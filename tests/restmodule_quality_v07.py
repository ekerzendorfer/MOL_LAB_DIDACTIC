"""DIDACTIC v0.7: SMARTS highlights, geometry-aware conformers, biomolecule scope."""
import contextlib
import io
import json
from pathlib import Path

import ipywidgets as widgets
from IPython.display import HTML
from rdkit import Chem

root=Path(__file__).resolve().parents[1]
nb=json.loads((root/"MOL_LAB_DIDACTIC_v0_4_2.ipynb").read_text(encoding="utf-8"))
code=next(c for c in nb["cells"] if c["cell_type"]=="code"
          and "def functional_group_highlight_widget(" in "".join(c["source"]))
ns={"__name__":"__didactic_v07_regression__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile("".join(code["source"]), "DIDACTIC main cell", "exec"), ns)
data=json.loads((root/"molecules_v0_4_2.json").read_text(encoding="utf-8"))
assert "v0.7-feinschliff-restmodule" in ns["DATA_URL"]
assert len(ns["MOLECULES"])==5
assert len(data["modules"]["Funktionelle Gruppen"])==13
assert len(data["modules"]["Konformere"])==7
assert len(data["modules"]["Wirkstoffe und Biomoleküle"])==11

# A ring selection must mean all aromatic atoms, not a single aromatic atom.
v=Chem.MolFromSmiles("COc1cc(C=O)ccc1O")
detected=ns["detect_functional_groups"](v)
assert {"Aromatischer Ring","Phenol","Aldehyd","Ether"}.issubset(set(detected))
ring_atoms,ring_bonds=ns["_functional_group_highlight_atoms"](v,"Aromatischer Ring")
assert len(ring_atoms)==6 and len(ring_bonds)==6
for group in ["Phenol","Aldehyd","Ether"]:
    atoms,bonds=ns["_functional_group_highlight_atoms"](v,group)
    assert len(atoms)>=2 and len(bonds)>=1,group
    assert atoms==sorted(set(atoms)) and bonds==sorted(set(bonds))
assert not ns["_functional_group_highlight_atoms"](v,"unbekannt")[0]
assert "Ether" not in ns["detect_functional_groups"](
    Chem.MolFromSmiles("CC(=O)OCC")), "Ester oxygen is not an ether group"
assert "Ether" not in ns["detect_functional_groups"](
    Chem.MolFromSmiles("CC(=O)OC(=O)C")), "Anhydride oxygen is not an ether group"
assert "Ester" in ns["detect_functional_groups"](
    Chem.MolFromSmiles("CC(=O)OCC"))
assert "Carbonsäure" in ns["detect_functional_groups"](
    Chem.MolFromSmiles("O=C(O)c1ccccc1O"))
assert "Phenol" in ns["detect_functional_groups"](
    Chem.MolFromSmiles("O=C(O)c1ccccc1O"))

# A single Colab widget updates in place, without redrawing 3D or changing molecules.
highlight=ns["functional_group_highlight_widget"](v,detected)
chooser, view=highlight.children[1],highlight.children[2]
assert chooser.value is None
assert "data:image/png" in view.value
raw_image=view.value
chooser.value="Phenol"
assert view.value!=raw_image
phenol_image=view.value
chooser.value="Aldehyd"
assert view.value!=phenol_image
chooser.value=None
assert view.value==raw_image

# Module user workflow: one independent structure viewer and normal quiz.
rendered=[]
ns["display"]=lambda *items: rendered.extend(items)
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value="Funktionelle Gruppen"
    ns["example_dd"].value="Vanillin"
    ns["run_btn"].click()
assert ns["current_report"]["type"]=="molecule"
assert ns["current_report"]["name"]=="Vanillin"
assert ns["current_report"]["assessment"] is None
panels=[x for x in rendered if isinstance(x,widgets.HBox)
        and len(x.children)==2
        and isinstance(x.children[0],widgets.VBox)
        and len(x.children[0].children)==4]
assert panels, "functional view not shown"
assert isinstance(panels[-1].children[1],widgets.HTML)
assert "3D-Modell" in panels[-1].children[1].value
# The same highlight works for curated drugs/biomolecules; sulfonamide is visible.
ace = Chem.MolFromSmiles("CC(=O)Nc1nnc(s1)S(N)(=O)=O")
assert "Sulfonamid" in ns["detect_functional_groups"](ace)
assert len(ns["_functional_group_highlight_atoms"](ace,"Sulfonamid")[0])>=4
rendered.clear()
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value="Wirkstoffe und Biomoleküle"
    ns["example_dd"].value="Acetazolamid"
    ns["run_btn"].click()
assert ns["current_report"]["name"]=="Acetazolamid"
drug_panels=[x for x in rendered if isinstance(x,widgets.HBox)
             and len(x.children)==2
             and isinstance(x.children[0],widgets.VBox)
             and len(x.children[0].children)==4]
assert drug_panels, "biomolecule highlight widget not displayed"
drug_picker=drug_panels[-1].children[0].children[1]
drug_view=drug_panels[-1].children[0].children[2]
assert "Sulfonamid" in [label for label, value in drug_picker.options]
base_image=drug_view.value
drug_picker.value="Sulfonamid"
assert drug_view.value!=base_image
drug_picker.value=None
assert drug_view.value==base_image

# Energy+geometry are both represented; no energy-only grouping.
with contextlib.redirect_stdout(io.StringIO()):
    mol,unique,all_rel=ns["generate_conformers"]("CCCC",n=28)
assert len(unique)>=2, "Butane anti/gauche minima should both appear"
assert len(unique)<=6
assert len(all_rel)>=len(unique)
names=[ns["_conformer_geometry_label"](mol,"CCCC",cid) for cid,e in unique]
assert all(x is not None for x in names)
assert any("anti" in x for x in names), names
assert any("gauche" in x for x in names), names
assert ns["_conformer_dihedral"](mol, "CCC", unique[0][0]) is None
with contextlib.redirect_stdout(io.StringIO()):
    molcl,cl,raw=ns["generate_conformers"]("ClCCCl",n=22)
assert cl and all(ns["_conformer_geometry_label"](molcl,"ClCCCl",cid) for cid,_ in cl)

# V0.7 MC content and pH/stereochemistry warnings must match JSON and fallback.
for compound in ["Paracetamol","Ibuprofen","Acetazolamid","Alanin","Phenylalanin"]:
    card=next(c for c in data["modules"]["Wirkstoffe und Biomoleküle"] if c["name"]==compound)
    fallback=ns["card_for"]("Wirkstoffe und Biomoleküle",compound)
    assert not card["frage"].startswith("Welche Aussage passt am besten")
    assert len(card["antworten"])==4 and card["richtig"]==0
    for field in ["frage","antworten","feedback","erklaerung","modellgrenze"]:
        assert fallback[field]==card[field],(compound,field)
    assert fallback["didaktik"]["mc_frage"]==card["frage"]
    assert fallback["didaktik"]["mc_antworten"]==card["antworten"]
for compound in ["Glycin","Alanin","Phenylalanin"]:
    card=ns["card_for"]("Wirkstoffe und Biomoleküle",compound)
    assert "Zwitterion" in card["modellgrenze"], compound
assert "offenkettige" in ns["card_for"]("Wirkstoffe und Biomoleküle","Ribose")["modellgrenze"]
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value="Wirkstoffe und Biomoleküle"
    ns["example_dd"].value="Alanin"
    ns["run_btn"].click()
assert ns["current_report"]["assessment"] is None
assert "Wasserlöslichkeits-Tendenz" not in ns["report_text"](ns["current_report"])

# Released v0.6 pair-first UX must still launch, without a first default pair.
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value="Isomerie"
assert ns["isomer_pair_dd"].value is None
with contextlib.redirect_stdout(io.StringIO()):
    ns["isomer_pair_dd"].value="Ethanol"
assert ns["current_report"]["type"]=="isomer_pair"
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value="Polarität und Löslichkeit"
    ns["polar_pair_dd"].value="Wasser vs. Schwefelwasserstoff"
assert ns["current_report"]["type"]=="polarity_pair"
print("V0.7: group highlight, SMARTS, conformers, biomolecule MC/limits, prior modules – OK")
