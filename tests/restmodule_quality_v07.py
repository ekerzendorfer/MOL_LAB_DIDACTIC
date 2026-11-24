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
assert any(b in ns["DATA_URL"] for b in ("/v0.7-feinschliff-restmodule/", "/v0.8-stereochemie-glucose/", "/main/"))
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

# A functional group takes precedence over its embedded C=O fragment.
aspirin=Chem.MolFromSmiles("CC(=O)Oc1ccccc1C(=O)O")
aspirin_groups=ns["detect_functional_groups"](aspirin)
assert "Carboxylgruppe" in aspirin_groups
assert "Ester" in aspirin_groups
assert "Carbonylgruppe" not in aspirin_groups,aspirin_groups
assert len(ns["_free_carbonyl_matches"](aspirin))==0
for smi in ["CC(=O)O","CC(=O)OC","CC(=O)OC(=O)C","CC(=O)N"]:
    mol_test=Chem.MolFromSmiles(smi)
    assert "Carbonylgruppe" not in ns["detect_functional_groups"](mol_test),smi
assert "Carbonylgruppe" in ns["detect_functional_groups"](
    Chem.MolFromSmiles("CC=O")), "Free aldehyde C=O remains selectable"

# Caffeine: delocalized fused aromatic system PLUS TWO explicit C=O groups.
caffeine=Chem.MolFromSmiles("Cn1cnc2n(C)c(=O)n(C)c(=O)c12")
caffeine_groups=ns["detect_functional_groups"](caffeine)
assert "Aromatischer Ring" in caffeine_groups
assert "Carbonylgruppe" in caffeine_groups,caffeine_groups
assert len(ns["_free_carbonyl_matches"](caffeine))==2
c_atoms,c_bonds=ns["_functional_group_highlight_atoms"](caffeine,"Carbonylgruppe")
assert len(c_atoms)==4 and len(c_bonds)==2
ring_atoms,ring_bonds=ns["_functional_group_highlight_atoms"](caffeine,"Aromatischer Ring")
assert len(ring_atoms)==9 and len(ring_bonds)==10
assert ns["_functional_group_display_label"](caffeine,"Aromatischer Ring")=="Aromatisches Ringsystem (RDKit)"
assert ns["_functional_group_display_label"](caffeine,"Carbonylgruppe")=="Ring-Carbonylgruppen (C=O)"
caffeine_ui=ns["functional_group_highlight_widget"](caffeine,caffeine_groups)
ui_values={value:label for label,value in caffeine_ui.children[1].options}
assert ui_values["Aromatischer Ring"]=="Aromatisches Ringsystem (RDKit)"
assert ui_values["Carbonylgruppe"]=="Ring-Carbonylgruppen (C=O)"
caffeine_ui.children[1].value="Carbonylgruppe"
assert "data:image/png" in caffeine_ui.children[2].value

# Adenine: both fused heterocyclic rings are recognized as aromatic by RDKit.
adenine=Chem.MolFromSmiles("Nc1ncnc2[nH]cnc12")
assert "Aromatischer Ring" in ns["detect_functional_groups"](adenine)
assert "Carbonylgruppe" not in ns["detect_functional_groups"](adenine)
a_atoms,a_bonds=ns["_functional_group_highlight_atoms"](adenine,"Aromatischer Ring")
assert len(a_atoms)==9 and len(a_bonds)==10
assert ns["_functional_group_display_label"](adenine,"Aromatischer Ring")=="Aromatisches Ringsystem (RDKit)"

assert "Ether" not in ns["detect_functional_groups"](
    Chem.MolFromSmiles("CC(=O)OCC")), "Ester oxygen is not an ether group"
assert "Ether" not in ns["detect_functional_groups"](
    Chem.MolFromSmiles("CC(=O)OC(=O)C")), "Anhydride oxygen is not an ether group"
assert "Ester" in ns["detect_functional_groups"](
    Chem.MolFromSmiles("CC(=O)OCC"))
assert "Carboxylgruppe" in ns["detect_functional_groups"](
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
