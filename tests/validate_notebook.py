"""Static audit for MOL_LAB DIDACTIC notebook and its curated JSON data."""
import ast
import json
from pathlib import Path

data = json.loads(Path("molecules_v0_4_2.json").read_text(encoding="utf-8"))
nb = json.loads(Path("MOL_LAB_DIDACTIC_v0_4_2.ipynb").read_text(encoding="utf-8"))
cell = next(c for c in nb["cells"] if c["cell_type"] == "code" and "FALLBACK_DATA = " in "".join(c["source"]))
source = "".join(cell["source"])
ast.parse(source)
assert "show_comparison_quiz(pair_quiz)" in source
nodes = [n for n in ast.parse(source).body if isinstance(n, ast.Assign)
         and any(isinstance(t, ast.Name) and t.id == "ISOMER_QUIZZES" for t in n.targets)]
assert len(nodes) == 1, "Missing structured isomer-specific questions"
isomer_quizzes = ast.literal_eval(nodes[0].value)
assert len(isomer_quizzes) == 7
for key, quiz in isomer_quizzes.items():
    assert key in data["isomer_pairs"], key
    assert quiz["frage"] and len(quiz["antworten"]) == 4, key
    assert 0 <= quiz["richtig"] < 4, key
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
assert any(c["id"] == "adenin" and c["smiles"] == "Nc1ncnc2[nH]cnc12" for c in data["modules"]["Wirkstoffe und Biomoleküle"]), "Adenine SMILES was reverted"
assert "'name': 'Adenin', 'smiles': 'Nc1ncnc2[nH]cnc12'" in source, "Adenine notebook fallback differs from JSON"
print("DIDACTIC: notebook syntax, 61 individual MCs, 7 polarity MCs, 7 isomer MCs and curated data – OK")
