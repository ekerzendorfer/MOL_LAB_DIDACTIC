"""Headless DIDACTIC UI regression, including the real 7 isomer pairs.

Uses ipywidgets + RDKit, but does not require a Colab browser session.
Checks the structure of emitted HTML and switches module/widget state.
"""
import contextlib
import io
import json
from pathlib import Path

from IPython.display import HTML
import ipywidgets as widgets

root = Path(__file__).resolve().parents[1]
nb = json.loads((root / "MOL_LAB_DIDACTIC_v0_4_2.ipynb").read_text(encoding="utf-8"))
main = next(cell for cell in nb["cells"] if cell["cell_type"] == "code"
            and "def display_isomer_comparison(" in "".join(cell["source"]))
code = "".join(main["source"])
ns = {"__name__": "__didactic_regression__"}
# The notebook initializes widgets when executed; capture text-only representations.
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(code, "DIDACTIC code cell", "exec"), ns)
assert len(ns["ISOMER_PAIR_OPTIONS"]) == 7
assert len(ns["ISOMER_QUIZZES"]) == 7
assert len(ns["MOLECULES"]) == 5

selected = []
ns["display"] = lambda *items: selected.extend(items)
counter = [0]
real_make3d = ns["make_3d"]
def spy3d(mol):
    counter[0] += 1
    return real_make3d(mol)
ns["make_3d"] = spy3d

name_a = "Propanal"
card_a = ns["card_for"]("Isomerie", name_a)
card_b = ns["card_for"]("Isomerie", "Aceton")
with contextlib.redirect_stdout(io.StringIO()):
    ns["display_isomer_comparison"](card_a, card_b)
assert counter[0] == 0, "3D generation must be lazy, not duplicated on page load"
html_parts = [obj.data for obj in selected if isinstance(obj, HTML)]
main_html = "".join(html_parts)
assert main_html.count("2D-Struktur") >= 2
assert "Propanal" in main_html and "Aceton" in main_html
assert "Struktur und funktionelle Gruppen" in main_html
assert "Experimentelle / kuratierte Stoffdaten" in main_html
assert "Qualitative Reaktivität" in main_html
assert "Weitere RDKit-Modellwerte" in main_html
assert "Wildman–Crippen" in main_html
assert "nicht hinterlegt" in main_html or "Wasserlöslichkeit" in main_html
assert "Didaktischer Polaritätseindruck" not in main_html
assert "pd.DataFrame" not in main_html

viewer = next(obj for obj in selected if isinstance(obj, widgets.VBox)
              and any(isinstance(x, widgets.HBox) for x in obj.children))
toolbar = next(x for x in viewer.children if isinstance(x, widgets.HBox))
choice, button = toolbar.children
assert isinstance(choice, widgets.ToggleButtons)
assert isinstance(button, widgets.Button)
assert len(choice.options) == 2
with contextlib.redirect_stdout(io.StringIO()):
    button.click()     # Generate exactly one molecule
assert counter[0] == 1, "3D button must generate only the selected structure"
with contextlib.redirect_stdout(io.StringIO()):
    choice.value = 1    # Replace viewer, never show both automatically
assert counter[0] == 2, "switching the displayed molecule should update the one viewer"

# Changing the module should reveal the guided pair selector and hide single controls.
ns["display"] = lambda *items: None
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value = "Isomerie"
assert ns["isomer_section"].layout.display != "none"
assert ns["single_section"].layout.display == "none"
assert ns["polar_section"].layout.display == "none"
assert ns["current_report"]["type"] == "isomer_pair"
assert ns["current_report"]["quiz"]["frage"] == ns["ISOMER_QUIZZES"][ns["isomer_pair_dd"].value]["frage"]

# Every curated isomer pair can be shown, with correct report and MC.
for label, left in ns["ISOMER_PAIR_OPTIONS"]:
    with contextlib.redirect_stdout(io.StringIO()):
        ns["isomer_pair_dd"].value = left
        ns["do_isomer_comparison"]()
    report = ns["current_report"]
    assert report["type"] == "isomer_pair", left
    assert len(report["cards"]) == 2
    assert report["quiz"]["frage"] == ns["ISOMER_QUIZZES"][left]["frage"]
    assert len(report["quiz"]["antworten"]) == 4
    text = ns["report_text"](report)
    assert report["cards"][0]["name"] in text
    assert report["cards"][1]["name"] in text
    assert "Didaktischer Polaritätseindruck" not in text
    assert "Wasserlöslichkeits-Tendenz" not in text
    quiz = report["quiz"]
    with contextlib.redirect_stdout(io.StringIO()):
        ns["answer_radio"].value = quiz["antworten"][quiz["richtig"]]
        ns["check_answer"]()
        ns["explain"]()
assert counter[0] == 2, "No 3D was supposed to be generated for the remaining pair tables"

# Optional individual work remains available; unrelated modules retain their controls.
with contextlib.redirect_stdout(io.StringIO()):
    ns["single_isomer_toggle"].value = True
assert ns["single_section"].layout.display != "none"
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value = "Konformere"
assert ns["single_section"].layout.display != "none"
assert ns["isomer_section"].layout.display == "none"
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value = "Polarität und Löslichkeit"
assert ns["polar_section"].layout.display != "none"
assert ns["single_section"].layout.display != "none"

assert len(nb["cells"]) == 5 and "Versions" not in "".join(nb["cells"][0]["source"])
print("DIDACTIC pair-first UI: 7 isomers, 1 lazy 3D viewer, pair MC, reports, other modules – OK")
