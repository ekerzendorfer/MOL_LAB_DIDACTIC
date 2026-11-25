"""DIDACTIC cyclohexane: three scientifically distinguished ring geometries."""
import contextlib
import io
import json
import math
from pathlib import Path

from rdkit import Chem
from rdkit.Chem import rdMolTransforms
from IPython.display import HTML
import pandas as pd
import ipywidgets as widgets

root=Path(__file__).resolve().parents[1]
data=json.loads((root/"molecules_v0_4_2.json").read_text(encoding="utf-8"))
nb=json.loads((root/"MOL_LAB_DIDACTIC_v0_4_2.ipynb").read_text(encoding="utf-8"))
code=next(c for c in nb["cells"] if c["cell_type"]=="code"
          and "def cyclohexane_reference_models(" in "".join(c["source"]))
ns={"__name__":"__cyclohexane_v08_regression__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile("".join(code["source"]), "DIDACTIC main cell", "exec"),ns)

card=next(c for c in data["modules"]["Konformere"] if c["name"]=="Cyclohexan")
fallback=ns["card_for"]("Konformere","Cyclohexan")
for key in ("leitfrage","beobachten","frage","antworten","richtig",
            "feedback","erklaerung","modellgrenze","didaktik"):
    assert fallback[key] == card[key], key
assert card["richtig"] == 2
assert "Twist-Boat" in card["frage"] or "Twist-Boat" in card["erklaerung"]
assert "Sattel" in card["modellgrenze"]
assert "Halbsessel" in card["modellgrenze"]

with contextlib.redirect_stdout(io.StringIO()):
    models=ns["cyclohexane_reference_models"]()
assert len(models)==3
assert [m["name"] for m in models]==["Sessel","Twist-Boat","Wanne"]
assert models[0]["delta_e"]==0
assert 4.5 < models[1]["delta_e"] < 7.5,models
assert 5.5 < models[2]["delta_e"] < 9.0,models
assert models[0]["delta_e"]<models[1]["delta_e"]<models[2]["delta_e"]
assert "globales Energieminimum" in models[0]["classification"]
assert "lokales Minimum" in models[1]["classification"]
assert "Sattel" in models[2]["classification"]
assert len(set(round(m["energy"],4) for m in models))==3

for shape in models:
    mol=shape["mol"]
    assert Chem.MolToSmiles(Chem.RemoveHs(mol))=="C1CCCCC1"
    assert mol.GetConformer().Is3D()
    assert len(shape["torsions"])==6
    assert all(math.isfinite(t) for t in shape["torsions"])
    abs_t=sorted(abs(t) for t in shape["torsions"])
    if shape["name"]=="Sessel":
        assert abs_t[0] > 40
        assert all(a*b<0 for a,b in zip(shape["torsions"],
                                        shape["torsions"][1:])),shape
    elif shape["name"]=="Wanne":
        assert abs_t[0]<10 and abs_t[1]<10 and abs_t[-1]>35
    else:
        assert 15<abs_t[0]<40 and abs_t[-1]>45
    for i in range(6):
        p=mol.GetConformer().GetAtomPosition(i)
        q=mol.GetConformer().GetAtomPosition((i+1)%6)
        assert 1.40 < p.Distance(q) < 1.65,(shape["name"],i,p.Distance(q))

# The visualizer must generate exactly 3 independent 3D frames, plus a
# model-only energy table and a caveat about the saddle geometry.
visual=[]
ns["display"]=lambda *items:visual.extend(items)
with contextlib.redirect_stdout(io.StringIO()):
    listed=ns["display_cyclohexane_reference_comparison"]()
assert len(listed)==3
panels=[x.data for x in visual if isinstance(x,HTML)
        and "ΔE(MMFF94)" in x.data]
assert len(panels)==1
assert panels[0].count("<iframe") == 3
assert all(shape in panels[0] for shape in ("Sessel","Twist-Boat","Wanne"))
tbl=[x for x in visual if isinstance(x,pd.DataFrame)]
assert len(tbl)==1 and len(tbl[0])==3
assert "Einordnung" in tbl[0].columns
assert any(isinstance(x,HTML) and "kein drittes stabiles Minimum" in x.data
           for x in visual)

# MW-024 path: same two clicks as before, but three curated shapes instead
# of the unstable random minimum-search output. Reporting and reset survive.
visual.clear()
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value="Konformere"
    ns["example_dd"].value="Cyclohexan"
    ns["run_btn"].click()
assert ns["current_report"]["name"]=="Cyclohexan"
assert "cyclohexane_geometries" not in ns["current_report"]
with contextlib.redirect_stdout(io.StringIO()):
    ns["conf_btn"].click()
report=ns["current_report"]
assert len(report["cyclohexane_geometries"])==3
assert report["cyclohexane_geometries"][2]["name"]=="Wanne"
protocol=ns["report_text"](report)
assert "Twist-Boat" in protocol and "Wanne" in protocol
assert "kein stabiles Minimum" in protocol
with contextlib.redirect_stdout(io.StringIO()):
    ns["reset3d_btn"].click()
assert len(ns["current_report"]["cyclohexane_geometries"])==3

# Other molecules retain their ordinary geometry-distinct minimum search.
with contextlib.redirect_stdout(io.StringIO()):
    ns["example_dd"].value="Butan"
    ns["run_btn"].click()
    ns["conf_btn"].click()
assert "cyclohexane_geometries" not in ns["current_report"]
print("Cyclohexan: Sessel, Twist-Boat, Wanne (Sattel) – geometrisch geprüft; MW-024 workflow OK")
