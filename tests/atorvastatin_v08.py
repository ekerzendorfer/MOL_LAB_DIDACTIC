"""Atorvastatin v0.8 regression: PubChem 60823, 2D, 3D, stereochemistry and quiz."""
import contextlib
import io
import json
from pathlib import Path
from IPython.display import HTML
import ipywidgets as widgets
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors

root=Path(__file__).resolve().parents[1]
data=json.loads((root/"molecules_v0_4_2.json").read_text(encoding="utf-8"))
nb=json.loads((root/"MOL_LAB_DIDACTIC_v0_4_2.ipynb").read_text(encoding="utf-8"))
code=next(c for c in nb["cells"] if c["cell_type"]=="code"
          and "def functional_group_highlight_widget(" in "".join(c["source"]))
ns={"__name__":"__atorvastatin_regression__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile("".join(code["source"]), "DIDACTIC cell", "exec"),ns)

bios=data["modules"]["Wirkstoffe und Biomoleküle"]
assert len(bios)==12
card=next(c for c in bios if c["name"]=="Atorvastatin")
assert card["id"]=="atorvastatin"
other=ns["card_for"]("Wirkstoffe und Biomoleküle","Atorvastatin")
for field in ["smiles","frage","antworten","feedback","erklaerung",
              "modellgrenze","didaktik","stoffdaten","reaktivitaet"]:
    assert other[field]==card[field],field
assert len(card["antworten"])==4 and card["richtig"]==1
assert "Calciumsalz" in card["modellgrenze"]
assert "PubChem CID 60823" in card["stoffdaten"]["quelle"]

mol=Chem.MolFromSmiles(card["smiles"])
assert mol is not None
assert rdMolDescriptors.CalcMolFormula(mol)=="C33H35FN2O5"
assert abs(Descriptors.MolWt(mol)-558.65)<0.01
assert mol.GetNumHeavyAtoms()==41
assert rdMolDescriptors.CalcNumRotatableBonds(mol)==12
assert mol.GetRingInfo().NumRings()==4
Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
assert [a.GetProp("_CIPCode") for a in mol.GetAtoms()
        if a.HasProp("_CIPCode")]==["R","R"]

groups=ns["detect_functional_groups"](mol)
for g in ("Alkohol","Carboxylgruppe","Amid","Aromatischer Ring","Arylfluorid"):
    assert g in groups,(g,groups)
for g in ("Ester","Amin","Carbonylgruppe"):
    assert g not in groups,(g,groups)
assert len(mol.GetSubstructMatches(Chem.MolFromSmarts(
    ns["FUNCTIONAL_GROUPS"]["Alkohol"])))==2
assert len(mol.GetSubstructMatches(Chem.MolFromSmarts(
    ns["FUNCTIONAL_GROUPS"]["Arylfluorid"])))==1

w=ns["functional_group_highlight_widget"](mol,groups)
picker,view=w.children[1],w.children[2]
assert w.layout.width=="510px"
assert view.layout.width=="500px"
assert "max-width:490px" in view.value
unmarked=view.value
picker.value="Carboxylgruppe"
assert view.value != unmarked
first=view.value
picker.value="Arylfluorid"
assert view.value != first
picker.value=None
assert view.value == unmarked

shown=[]
ns["display"]=lambda *items: shown.extend(items)
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value="Wirkstoffe und Biomoleküle"
    ns["example_dd"].value="Atorvastatin"
    ns["run_btn"].click()
rep=ns["current_report"]
assert rep["type"]=="molecule" and rep["name"]=="Atorvastatin"
assert len([x for x in shown if isinstance(x,HTML)
            and "Komplexität auf einen Blick" in x.data])==1
assert any(isinstance(x,widgets.HBox)
           and len(x.children)==2
           and isinstance(x.children[0],widgets.VBox)
           and x.children[0].layout.width=="510px" for x in shown)
assert "Arylfluorid" in rep["groups"]
with contextlib.redirect_stdout(io.StringIO()):
    ns["answer_radio"].value=card["antworten"][card["richtig"]]
    ns["check_btn"].click()
assert "Richtig" in ns["feedback_html"].value
with contextlib.redirect_stdout(io.StringIO()):
    ns["explain_btn"].click()
assert "Fachliche Erklärung" in ns["feedback_html"].value
protocol=ns["report_text"](rep)
assert "Atorvastatin" in protocol
assert "PubChem CID 60823" in protocol
assert "Calciumsalz" in protocol
print("Atorvastatin: 41 heavy atoms, R/R, 4 rings, 12 rotatable, large 2D, MC, report – OK")
