"""Static audit for MOL_LAB DIDACTIC notebook and its curated JSON data."""
import ast
import json
from pathlib import Path

data = json.loads(Path("molecules_v0_4_2.json").read_text(encoding="utf-8"))
nb = json.loads(Path("MOL_LAB_DIDACTIC_v0_4_2.ipynb").read_text(encoding="utf-8"))
cell = next(c for c in nb["cells"] if c["cell_type"] == "code" and "FALLBACK_DATA = " in "".join(c["source"]))
source = "".join(cell["source"])
ast.parse(source)
assert "show_comparison_quiz(card_a)" in source
assert "show_comparison_quiz(pair[\"quiz\"])" in source
assert "random.shuffle(answers)" in source

cards = [c for items in data["modules"].values() for c in items]
assert len(cards) == 61, "Unexpected change in curated molecule count"
for card in cards:
    quiz = card
    assert quiz.get("frage") and len(quiz.get("antworten", [])) == 4, card.get("name")
    assert isinstance(quiz.get("richtig"), int) and 0 <= quiz["richtig"] < 4, card.get("name")
assert len(data["polarity_pairs"]) == 7
for name, pair in data["polarity_pairs"].items():
    quiz = pair.get("quiz", {})
    assert quiz.get("frage") and len(quiz.get("antworten", [])) == 4, name
    assert isinstance(quiz.get("richtig"), int) and 0 <= quiz["richtig"] < 4, name
assert any(c["id"] == "propanal" and c["stoffdaten"]["siedepunkt_C"] for c in data["modules"]["Isomerie"])
assert "48–49" in source and "Propanal" in source
print("DIDACTIC: notebook Python syntax, 61 molecule MCs, 7 comparison MCs, Propanal data – OK")
