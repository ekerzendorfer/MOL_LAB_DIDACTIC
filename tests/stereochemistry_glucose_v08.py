"""Scientific/interactive tests for v0.8 stereo pairs and D-glucose forms."""
import contextlib
import io
import json
from pathlib import Path

from IPython.display import HTML
import ipywidgets as widgets
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors

root=Path(__file__).resolve().parents[1]
nb=json.loads((root/"MOL_LAB_DIDACTIC_v0_4_2.ipynb").read_text(encoding="utf-8"))
main=next(c for c in nb["cells"] if c["cell_type"]=="code"
          and "def do_glucose_explorer(" in "".join(c["source"]))
ns={"__name__":"__stereo_v08_regression__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile("".join(main["source"]), "DIDACTIC main code", "exec"), ns)

assert len(ns["ISOMER_PAIR_OPTIONS"])==8  # original seven, no silent extra pair
labels={name:value for name,value in ns["ISOMER_PAIR_OPTIONS"]}
assert any("Enantiomerie" in label for label in labels)
assert any("E/Z-Stereoisomerie" in label for label in labels)
assert len(ns["ISOMER_QUIZZES"])==7
assert ns["isomer_pair_dd"].value is None

def smiles_mol(mod,name):
    return ns["mol_from_smiles"](ns["card_for"](mod,name)["smiles"])

d=smiles_mol("Isomerie","D-Alanin")
l=smiles_mol("Isomerie","L-Alanin")
assert ns["_isomer_pair_kind"]("D-Alanin","L-Alanin")=="enantiomers"
assert ns["_isomer_pair_kind"]("Maleinsäure","Fumarsäure")=="ez"
assert ns["_isomer_pair_kind"]("Ethanol","Dimethylether")=="constitutional"
assert len(ns["_stereo_pair_markings"](d,"enantiomers")[0])==1
assert len(ns["_stereo_pair_markings"](l,"enantiomers")[0])==1
assert [a.GetProp("_CIPCode") for a in d.GetAtoms() if a.HasProp("_CIPCode")]==["R"]
assert [a.GetProp("_CIPCode") for a in l.GetAtoms() if a.HasProp("_CIPCode")]==["S"]
essay=ns["_stereo_pair_explanation"]({"name":"D-Alanin"},{"name":"L-Alanin"},d,l)
assert "D-Alanin (R)" in essay and "L-Alanin (S)" in essay
assert "nicht generell R" in essay
for name, expected in (("Maleinsäure","Z"),("Fumarsäure","E")):
    mol=smiles_mol("Isomerie",name)
    focused,bonds=ns["_stereo_pair_markings"](mol,"ez")
    assert len(focused)==4 and len(bonds)==1
    assert "STEREO"+expected in str(mol.GetBondWithIdx(bonds[0]).GetStereo())
    assert ns["_stereo_pair_explanation"](
        {"name":"Maleinsäure"},{"name":"Fumarsäure"},
        smiles_mol("Isomerie","Maleinsäure"),
        smiles_mol("Isomerie","Fumarsäure")
    ).count("E/Z")>=1

# 3 authentic stereospecified structures; four centres in open, five in ring.
forms=ns["GLUCOSE_FORMS"]
assert set(forms)=={"open","alpha","beta"}
mols={k:Chem.MolFromSmiles(v["smiles"]) for k,v in forms.items()}
assert all(m is not None for m in mols.values())
assert {rdMolDescriptors.CalcMolFormula(m) for m in mols.values()}=={"C6H12O6"}
assert mols["open"].GetRingInfo().NumRings()==0
assert mols["alpha"].GetRingInfo().NumRings()==1
assert mols["beta"].GetRingInfo().NumRings()==1
assert sorted(len(ring) for ring in mols["alpha"].GetRingInfo().AtomRings())==[6]
def chiral(m):
    Chem.AssignStereochemistry(m, cleanIt=True,force=True)
    return {a.GetIdx():a.GetProp("_CIPCode") for a in m.GetAtoms()
            if a.HasProp("_CIPCode")}
open_cip=chiral(mols["open"])
alpha_cip=chiral(mols["alpha"])
beta_cip=chiral(mols["beta"])
assert len(open_cip)==4 and len(alpha_cip)==len(beta_cip)==5
assert {2: "R", 4:"R", 6:"S", 8:"R"}==open_cip
assert alpha_cip[5]=="S" and beta_cip[5]=="R"
assert {i:code for i,code in alpha_cip.items() if i!=5}=={
    i:code for i,code in beta_cip.items() if i!=5
}
assert set(forms["open"]["focus"])=={3,10,11}
assert all(set(forms[k]["focus"])=={5,6,7} for k in ("alpha","beta"))
assert mols["open"].GetBondBetweenAtoms(10,11).GetBondTypeAsDouble()==2
assert all(mols[k].GetAtomWithIdx(6).IsInRing() for k in ("alpha","beta"))
assert all("PubChem CID" in v["quelle"] for v in forms.values())

# The user explicitly opens Glucose; changing stages must not affect the seven pairs.
seen=[]
ns["display"]=lambda *items:seen.extend(items)
created=[0]
old_make3d=ns["make_3d"]
def track3d(mol):
    created[0]+=1
    return old_make3d(mol)
ns["make_3d"]=track3d
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value="Isomerie"
assert ns["isomer_pair_dd"].value is None
with contextlib.redirect_stdout(io.StringIO()):
    ns["glucose_btn"].click()
assert created[0]==0,"3D should remain lazy"
report=ns["current_report"]
assert report["type"]=="glucose_equilibrium"
assert len(report["cards"])==3
assert report["quiz"]==ns["GLUCOSE_QUIZ"]
assert report["glucose_stage"]=="open"
selection=next(w for w in seen if isinstance(w,widgets.VBox) and len(w.children)==3
               and isinstance(w.children[0],widgets.ToggleButtons)
               and [v for label,v in w.children[0].options]==[
                   "open","alpha","beta","compare"])
stage,info,panel=selection.children
assert stage.value=="open" and len(panel.children)==1
assert "C1" in info.value and "C5" in info.value
stage.value="alpha"
assert report["glucose_stage"]=="alpha"
assert len(panel.children)==1 and isinstance(panel.children[0],widgets.HBox)
assert len(panel.children[0].children)==2
assert "Halbacetal" not in info.value or "C1" in info.value
stage.value="beta"
assert report["glucose_stage"]=="beta"
stage.value="compare"
assert report["glucose_stage"]=="compare" and "Diastereomere" in info.value
assert len(panel.children[0].children)==2
alpha_card,beta_card=panel.children[0].children
assert "α-D-Glucopyranose" in alpha_card.children[0].value
assert "β-D-Glucopyranose" in beta_card.children[0].value
with contextlib.redirect_stdout(io.StringIO()):
    alpha_card.children[1].value="3d"
assert created[0]==1
with contextlib.redirect_stdout(io.StringIO()):
    alpha_card.children[1].value="2d"
assert "data:image/png" in alpha_card.children[2].value
assert ns["current_report"]["type"]=="glucose_equilibrium"
quiz=report["quiz"]
with contextlib.redirect_stdout(io.StringIO()):
    ns["answer_radio"].value=quiz["antworten"][quiz["richtig"]]
    ns["check_btn"].click()
assert "Richtig" in ns["feedback_html"].value
with contextlib.redirect_stdout(io.StringIO()):
    ns["explain_btn"].click()
assert "Fachliche Erklärung" in ns["feedback_html"].value
assert "Offenkettige D-Glucose" in ns["report_text"](report)
assert "α-D-Glucopyranose" in ns["report_text"](report)
assert "β-D-Glucopyranose" in ns["report_text"](report)
with contextlib.redirect_stdout(io.StringIO()):
    ns["reset3d_btn"].click()
assert ns["current_report"]["glucose_stage"]=="compare"

# Pair after explorer must clear old report; previous modules stay accessible.
with contextlib.redirect_stdout(io.StringIO()):
    ns["isomer_pair_dd"].value="D-Alanin"
assert ns["current_report"]["type"]=="isomer_pair"
assert "D-Alanin" in ns["current_report"]["title"]
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value="Wirkstoffe und Biomoleküle"
    ns["example_dd"].value="Acetazolamid"
    ns["run_btn"].click()
assert ns["current_report"]["type"]=="molecule"
assert "Sulfonamid" in ns["current_report"]["groups"]
print("V0.8: stereochemistry CIP/EZ, 3 glucose structures, guided workflow, reports, prior modules – OK")
