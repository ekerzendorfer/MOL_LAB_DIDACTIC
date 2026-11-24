"""Headless V0.5 Isomerie regression, including all seven curated pairs.

Tests the same ipywidgets callbacks that the learner uses in Colab:
conscious selection, in-place 2D/3D/surface tabs, local MC feedback, notes
and unchanged single-molecule controls in unrelated modules.
"""
import contextlib
import io
import json
from pathlib import Path
from IPython.display import HTML
import ipywidgets as widgets

root = Path(__file__).resolve().parents[1]
notebook = json.loads((root / "MOL_LAB_DIDACTIC_v0_4_2.ipynb").read_text(encoding="utf-8"))
main = next(cell for cell in notebook["cells"] if cell["cell_type"] == "code"
            and "def display_isomer_comparison(" in "".join(cell["source"]))
ns = {"__name__": "__didactic_regression__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile("".join(main["source"]), "DIDACTIC code cell", "exec"), ns)
assert len(ns["ISOMER_PAIR_OPTIONS"]) == 8, "7 pairs plus explicit choose placeholder"
assert ns["ISOMER_PAIR_OPTIONS"][0][1] is None
assert len(ns["ISOMER_QUIZZES"]) == 7
assert len(ns["MOLECULES"]) == 5
assert ns["isomer_pair_dd"].value is None

selected = []
ns["display"] = lambda *items: selected.extend(items)
counter = [0]
rendered_styles = []
real_make3d = ns["make_3d"]
real_iframe = ns["mol3d_iframe_html"]
def spy3d(mol):
    counter[0] += 1
    return real_make3d(mol)
def spyframe(mol, **kw):
    rendered_styles.append(kw.get("style"))
    return real_iframe(mol, **kw)
ns["make_3d"] = spy3d
ns["mol3d_iframe_html"] = spyframe

p = ns["card_for"]("Isomerie", "Propanal")
a = ns["card_for"]("Isomerie", "Aceton")
with contextlib.redirect_stdout(io.StringIO()):
    ns["display_isomer_comparison"](p, a)
assert counter[0] == 0, "3D must not be built without deliberate selection"
html_parts = [x.data for x in selected if isinstance(x, HTML)]
page_html = "".join(html_parts)
assert "Propanal" in page_html and "Aceton" in page_html
assert "Struktur und funktionelle Gruppen" in page_html
assert "Experimentelle / kuratierte Stoffdaten" in page_html
assert "Qualitative Reaktivität" in page_html
assert "Weitere RDKit-Modellwerte" in page_html
assert "Wildman–Crippen" in page_html
assert "Didaktischer Polaritätseindruck" not in page_html

cards = next(obj for obj in selected if isinstance(obj, widgets.HBox)
             and len(obj.children) == 2
             and all(isinstance(x, widgets.VBox) for x in obj.children))
assert len(cards.children) == 2
for card in cards.children:
    title, toggle, image = card.children
    assert isinstance(title, widgets.HTML)
    assert isinstance(toggle, widgets.ToggleButtons)
    assert [value for label, value in toggle.options] == ["2d", "3d", "surface"]
    assert isinstance(image, widgets.HTML)
    assert "2D-Struktur" in image.value and "data:image/png" in image.value
left, right = cards.children
with contextlib.redirect_stdout(io.StringIO()):
    left.children[1].value = "3d"
assert counter[0] == 1 and "<iframe" in left.children[2].value
assert "2D-Struktur" in right.children[2].value
with contextlib.redirect_stdout(io.StringIO()):
    left.children[1].value = "surface"
assert counter[0] == 1, "surface must reuse cached conformer"
assert rendered_styles[-1] == "Didaktische Polaritätsoberfläche"
assert "keine" in left.children[2].value.lower()
with contextlib.redirect_stdout(io.StringIO()):
    left.children[1].value = "2d"
assert "2D-Struktur" in left.children[2].value
with contextlib.redirect_stdout(io.StringIO()):
    right.children[1].value = "3d"
assert counter[0] == 2, "each molecule is calculated independently on first request"

ns["display"] = lambda *items: None
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value = "Isomerie"
assert ns["isomer_section"].layout.display != "none"
assert ns["single_section"].layout.display == "none"
assert ns["polar_section"].layout.display == "none"
assert ns["isomer_pair_dd"].value is None
assert not ns["current_report"], "module selection must NOT launch first pair"

for label, left in ns["ISOMER_PAIR_OPTIONS"][1:]:
    with contextlib.redirect_stdout(io.StringIO()):
        ns["isomer_pair_dd"].value = left
    assert not ns["current_report"], "dropdown alone must not launch an analysis"
    with contextlib.redirect_stdout(io.StringIO()):
        ns["compare_btn"].click()
    report = ns["current_report"]
    assert report["type"] == "isomer_pair", left
    assert len(report["cards"]) == 2
    assert report["quiz"]["frage"] == ns["ISOMER_QUIZZES"][left]["frage"]
    assert len(report["quiz"]["antworten"]) == 4
    txt = ns["report_text"](report)
    assert report["cards"][0]["name"] in txt
    assert report["cards"][1]["name"] in txt
    assert "Didaktischer Polaritätseindruck" not in txt
    quiz = report["quiz"]
    with contextlib.redirect_stdout(io.StringIO()):
        ns["check_btn"].click() # No answer yet: informative inline response
    assert "Bitte zuerst" in ns["feedback_html"].value
    with contextlib.redirect_stdout(io.StringIO()):
        ns["answer_radio"].value = quiz["antworten"][quiz["richtig"]]
        ns["check_btn"].click()
    assert "Richtig" in ns["feedback_html"].value
    with contextlib.redirect_stdout(io.StringIO()):
        ns["explain_btn"].click()
    assert "Fachliche Erklärung" in ns["feedback_html"].value
assert counter[0] == 2, "tab views, not comparison table, may generate 3D"

# Optional single work and other modules remain operational.
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

assert len(notebook["cells"]) == 5
print("V0.5 UI: 7 pairs, explicit choice, two in-place 2D/3D/surface tabs, immediate MC feedback, other modules – OK")
