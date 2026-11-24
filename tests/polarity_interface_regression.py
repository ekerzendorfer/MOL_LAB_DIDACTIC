"""Regression for v0.6 polarity cards, quiz, report, fallback and functional groups."""
import contextlib
import io
import json
from pathlib import Path

import ipywidgets as widgets
from IPython.display import HTML
from rdkit import Chem

root = Path(__file__).resolve().parents[1]
nb = json.loads((root / "MOL_LAB_DIDACTIC_v0_4_2.ipynb").read_text(encoding="utf-8"))
code = next(c for c in nb["cells"] if c["cell_type"] == "code"
            and "def display_polarity_comparison(" in "".join(c["source"]))
ns = {"__name__": "__didactic_polarity_regression__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile("".join(code["source"]), "DIDACTIC notebook", "exec"), ns)
data = json.loads((root / "molecules_v0_4_2.json").read_text(encoding="utf-8"))
assert len(data["polarity_pairs"]) == 7
assert len(ns["POLARITY_PAIRS"]) == 7
assert ns["polar_pair_dd"].value is None
assert ns["DATA_URL"].endswith("/molecules_v0_4_2.json")
assert "/main/" in ns["DATA_URL"] or "/v0.7-feinschliff-restmodule/" in ns["DATA_URL"] or "/v0.8-stereochemie-glucose/" in ns["DATA_URL"]
assert len(ns["MOLECULES"]) == 5
butan = next(c for c in data["modules"]["Konformere"] if c["name"] == "Butan")
butan_runtime = ns["card_for"]("Konformere", "Butan")
assert butan_runtime["frage"] == butan["frage"]
assert butan_runtime["antworten"] == butan["antworten"]
assert "anti" in butan["frage"] and "gauche" in butan["frage"]
assert butan_runtime["didaktik"]["mc_frage"] == butan["didaktik"]["mc_frage"]

def matches(smiles, group):
    return group in ns["detect_functional_groups"](Chem.MolFromSmiles(smiles))
assert matches("C=O", "Aldehyd")                  # Methanal
assert matches("CC=O", "Aldehyd")                 # Ethanal
assert not matches("CC(=O)C", "Aldehyd")          # Keton
assert matches("CC(=O)OC", "Ester")              # Methylacetat
assert matches("CC(=O)Oc1ccccc1", "Ester")       # Arylester
assert not matches("CC(=O)OC(=O)C", "Ester")      # Anhydrid
assert matches("CC(=O)OC(=O)C", "Carbonsäureanhydrid")

# A pair must begin in 2D with separate lazy cards, not precalculated 3D.
selected = []
ns["display"] = lambda *items: selected.extend(items)
count = [0]
orig_3d = ns["make_3d"]
def spy3d(mol):
    count[0] += 1
    return orig_3d(mol)
ns["make_3d"] = spy3d
with contextlib.redirect_stdout(io.StringIO()):
    ns["display_polarity_comparison"]("Wasser vs. Schwefelwasserstoff")
assert count[0] == 0
html_all = "".join(x.data for x in selected if isinstance(x, HTML))
assert "Experimentelle / kuratierte Stoffdaten" in html_all
assert "Weitere RDKit-Modellwerte" in html_all
assert "Quellen / Bedingungen" in html_all
assert "Van-der-Waals" in html_all
assert "Wasserlöslichkeits-Tendenz" not in html_all
cards = next(x for x in selected if isinstance(x, widgets.HBox)
             and len(x.children)==2 and
             all(isinstance(c, widgets.VBox) for c in x.children))
for card in cards.children:
    title, toggle, view = card.children
    assert card.layout.width == "475px"
    assert [value for label, value in toggle.options] == ["2d", "3d", "surface"]
    assert "data:image/png" in view.value
with contextlib.redirect_stdout(io.StringIO()):
    cards.children[0].children[1].value = "3d"
assert count[0] == 1 and "<iframe" in cards.children[0].children[2].value
with contextlib.redirect_stdout(io.StringIO()):
    cards.children[0].children[1].value = "surface"
assert count[0] == 1 and "SurfaceType.VDW" in cards.children[0].children[2].value
with contextlib.redirect_stdout(io.StringIO()):
    cards.children[0].children[1].value = "2d"
assert "data:image/png" in cards.children[0].children[2].value

# Module selection must not launch a pair, but selecting any of the seven does.
ns["display"] = lambda *items: None
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value = "Polarität und Löslichkeit"
assert ns["polar_pair_dd"].value is None
assert not ns["current_report"]
assert ns["polar_section"].layout.display != "none"
assert ns["single_section"].layout.display != "none", "MW-015 still needs single analysis"
for key in data["polarity_pairs"]:
    with contextlib.redirect_stdout(io.StringIO()):
        ns["polar_pair_dd"].value = key
    report = ns["current_report"]
    assert report["type"] == "polarity_pair" and report["title"] == key
    assert len(report["cards"]) == 2
    assert report["assessments"] == [None, None]
    quiz = report["quiz"]
    assert len(quiz["antworten"]) == 4
    txt = ns["report_text"](report)
    assert "Wasserlöslichkeits-Tendenz" not in txt
    assert "Didaktischer Polaritätseindruck" not in txt
    with contextlib.redirect_stdout(io.StringIO()):
        ns["check_btn"].click()
    assert "Bitte zuerst" in ns["feedback_html"].value
    with contextlib.redirect_stdout(io.StringIO()):
        ns["answer_radio"].value = quiz["antworten"][quiz["richtig"]]
        ns["check_btn"].click()
    assert "Richtig" in ns["feedback_html"].value
    with contextlib.redirect_stdout(io.StringIO()):
        ns["explain_btn"].click()
    assert "Fachliche Erklärung" in ns["feedback_html"].value
assert count[0] == 1, "3D only after explicit tab click"

# Pair/single switching, 3D reset and other modules should remain valid.
with contextlib.redirect_stdout(io.StringIO()):
    ns["example_dd"].value = "Methanol"
assert ns["polar_pair_dd"].value is None
with contextlib.redirect_stdout(io.StringIO()):
    ns["run_btn"].click()
assert ns["current_report"]["type"] == "molecule"
assert ns["current_report"]["name"] == "Methanol"
with contextlib.redirect_stdout(io.StringIO()):
    ns["polar_pair_dd"].value = "Aceton vs. Essigsäure"
assert ns["current_report"]["type"] == "polarity_pair"
with contextlib.redirect_stdout(io.StringIO()):
    ns["reset3d_btn"].click()
assert ns["current_report"]["type"] == "polarity_pair"
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value = "Konformere"
assert ns["single_section"].layout.display != "none"
assert ns["polar_section"].layout.display == "none"
print("V0.6: 7 polarity pairs, lazy 2D/3D/surface, MC/report, Butan, SMARTS, single-mode – OK")
