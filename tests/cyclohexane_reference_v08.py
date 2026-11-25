"""DIDACTIC cyclohexane: four scientifically distinguished ring geometries."""
import contextlib
import io
import json
import math
from pathlib import Path

from rdkit import Chem
from rdkit.Chem import rdMolTransforms, AllChem
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
assert "Hesse" in card["modellgrenze"]

with contextlib.redirect_stdout(io.StringIO()):
    models=ns["cyclohexane_reference_models"]()
assert len(models)==4
assert [m["name"] for m in models]==["Sessel","Twist-Boat","Wanne","Halbsessel"]
assert models[0]["delta_e"]==0
assert 4.5 < models[1]["delta_e"] < 7.5,models
assert 5.5 < models[2]["delta_e"] < 9.0,models
assert models[0]["delta_e"]<models[1]["delta_e"]<models[2]["delta_e"]<models[3]["delta_e"]
assert 8.5 < models[3]["delta_e"] < 13.5,models
assert "globales Energieminimum" in models[0]["classification"]
assert "lokales Minimum" in models[1]["classification"]
assert "Sattel" in models[2]["classification"]
assert "kein Minimum" in models[3]["classification"]
assert [m["geometry_restrained"] for m in models]==[False,False,False,True]
assert len(set(round(m["energy"],4) for m in models))==4

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
    elif shape["name"]=="Halbsessel":
        assert abs_t[0]<12 and abs_t[-1]>50
        # Four consecutive carbons remain nearly coplanar; the two adjacent
        # flaps lie on opposite sides of that plane.
        zs=[mol.GetConformer().GetAtomPosition(i).z for i in range(6)]
        assert all(abs(z)<0.13 for z in zs[:4]),zs
        assert zs[4] > .22 and zs[5] < -.22,zs
        # Without restraint a minimum search must leave the half-chair.
        free=Chem.Mol(mol)
        props=AllChem.MMFFGetMoleculeProperties(free)
        ff=AllChem.MMFFGetMoleculeForceField(free,props)
        assert ff.Minimize(maxIts=900)==0
        assert ff.CalcEnergy()<shape["energy"]-3.0
    else:
        assert 15<abs_t[0]<40 and abs_t[-1]>45
    for i in range(6):
        p=mol.GetConformer().GetAtomPosition(i)
        q=mol.GetConformer().GetAtomPosition((i+1)%6)
        assert 1.40 < p.Distance(q) < 1.65,(shape["name"],i,p.Distance(q))

# The visualizer must generate exactly 4 independent 3D frames, plus a
# model-only energy table and a caveat about the saddle geometry.
visual=[]
ns["display"]=lambda *items:visual.extend(items)
with contextlib.redirect_stdout(io.StringIO()):
    listed=ns["display_cyclohexane_reference_comparison"]()
assert len(listed)==4
panels=[x.data for x in visual if isinstance(x,HTML)
        and "ΔE(MMFF94)" in x.data]
assert len(panels)==1
assert panels[0].count("<iframe") == 4
assert all(shape in panels[0] for shape in ("Sessel","Twist-Boat","Wanne","Halbsessel"))
tbl=[x.data for x in visual if isinstance(x,HTML)
     and "class='cyclo-energy-table'" in x.data]
assert len(tbl)==1 and tbl[0].count("<tr>")==4
assert "Einordnung" in tbl[0]
assert all(m["classification"] in tbl[0] for m in models)
assert "white-space:normal" in tbl[0]
assert "fixierte Annäherung an eine Übergangslage (kein Minimum)" in tbl[0]
details=[x.data for x in visual if isinstance(x,HTML)
         and "Was zeigen die vier Ringformen?" in x.data]
assert len(details)==1 and " open>" not in details[0]
assert any(isinstance(x,HTML) and "kein drittes stabiles Minimum" in x.data
           for x in visual)

# MW-024 path: same two clicks as before, but four curated shapes instead
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
assert len(report["cyclohexane_geometries"])==4
assert report["cyclohexane_geometries"][2]["name"]=="Wanne"
assert report["cyclohexane_geometries"][3]["name"]=="Halbsessel"
protocol=ns["report_text"](report)
assert all(n in protocol for n in ("Sessel","Twist-Boat","Wanne","Halbsessel"))
assert "kein stabiles Minimum" in protocol
with contextlib.redirect_stdout(io.StringIO()):
    ns["reset3d_btn"].click()
assert len(ns["current_report"]["cyclohexane_geometries"])==4

# Other molecules retain their ordinary geometry-distinct minimum search.
with contextlib.redirect_stdout(io.StringIO()):
    ns["example_dd"].value="Butan"
    ns["run_btn"].click()
    ns["conf_btn"].click()
assert "cyclohexane_geometries" not in ns["current_report"]
print("Cyclohexan: 4 Formen inkl. restringiertem Halbsessel – geometrisch geprüft; MW-024 workflow OK")
