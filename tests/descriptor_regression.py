"""RDKit descriptors of all DIDACTIC source cards: computation integrity, not experimental validation.

The test pins the model definitions and explicitly checks the acetone/propanal
limitation. DO NOT change logP values to match literature measurements.
"""
import json
import math
from pathlib import Path

from rdkit import Chem, rdBase
from rdkit.Chem import Crippen, Descriptors, rdMolDescriptors

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "molecules_v0_4_2.json").read_text(encoding="utf-8"))
cards = [(module, card) for module, items in data["modules"].items() for card in items]
assert len(cards) == 61, f"Unexpected source count: {len(cards)}"

invalid = []
descriptors = {}
for module, card in cards:
    smiles = card["smiles"]
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        invalid.append((module, card["name"], smiles))
        continue
    values = {
        "formula": rdMolDescriptors.CalcMolFormula(mol),
        "mass": Descriptors.MolWt(mol),
        "logp": Crippen.MolLogP(mol),
        "tpsa": rdMolDescriptors.CalcTPSA(mol),
        "rotatable": rdMolDescriptors.CalcNumRotatableBonds(mol),
        "donors": rdMolDescriptors.CalcNumHBD(mol),
        "acceptors": rdMolDescriptors.CalcNumHBA(mol)
    }
    assert all(math.isfinite(v) for k, v in values.items() if isinstance(v, float)), card["name"]
    descriptors[(module, card["name"])] = values

assert not invalid, "Invalid DIDACTIC SMILES: " + repr(invalid)
assert len(descriptors) == 61
p = descriptors[("Isomerie", "Propanal")]
a = descriptors[("Isomerie", "Aceton")]
assert p["formula"] == a["formula"] == "C3H6O"
assert abs(p["mass"]-58.08) < 0.02 and abs(a["mass"]-58.08) < 0.02
assert abs(p["tpsa"] - 17.07) < 1e-4
assert abs(a["tpsa"] - 17.07) < 1e-4
assert abs(p["logp"] - 0.5953) < 1e-4
assert abs(a["logp"] - 0.5953) < 1e-4
assert (p["rotatable"], a["rotatable"]) == (1, 0)
assert Chem.MolFromSmiles(next(c["smiles"] for _, c in cards if c["name"]=="Adenin")) is not None

pairs = data["isomer_pairs"]
seen = set()
for name, other in pairs.items():
    key = tuple(sorted((name, other)))
    assert pairs[other] == name, f"Non-reciprocal isomer pair {name}: {other}"
    if key in seen:
        continue
    seen.add(key)
    m1 = descriptors[("Isomerie", name)]
    m2 = descriptors[("Isomerie", other)]
    assert m1["formula"] == m2["formula"], f"Different molecular formulas in pair {key}"
assert len(seen) == 7, seen

print(f"RDKit {rdBase.rdkitVersion} – {len(cards)} cards and 7 isomer pairs validated")
print("Propanal/acetone: model logP = %.4f / %.4f; TPSA = %.2f / %.2f; rotatable = %d / %d" %
      (p["logp"], a["logp"], p["tpsa"], a["tpsa"], p["rotatable"], a["rotatable"]))
print("Note: atom-contribution logP, topology-only TPSA and rotatable-bond definition")
print("are NOT experimental properties, and must not be used as universal isomer discriminators.")
