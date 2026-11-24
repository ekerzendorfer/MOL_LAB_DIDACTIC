# DIDACTIC v0.5 – Abnahme der neuen Isomerie-Ansicht

**Stand:** 24.11.2026 · **Entwicklungszweig:** `v0.5-isomerien-vergleich`  
**Status:** Automatische Chemie-, Daten-, Notebook- und Widgettests erfolgreich. **Visueller Colab-Test steht noch aus.** Die stabile `main`-Version bleibt unverändert.

## Isolierter Test in Colab

- [Entwicklungsnotebook direkt in Colab öffnen](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/v0.5-isomerien-vergleich/MOL_LAB_DIDACTIC_v0_4_2.ipynb)
- Alternativ die [Notebook-Datei auf dem Entwicklungszweig](https://github.com/ekerzendorfer/MOL_LAB_DIDACTIC/blob/v0.5-isomerien-vergleich/MOL_LAB_DIDACTIC_v0_4_2.ipynb) öffnen.
- **Laufzeit → Alle ausführen**. Keine Ausführung in einer älteren, noch aktiven Laufzeit voraussetzen.

Der Dateiname bleibt aus Kompatibilitätsgründen `MOL_LAB_DIDACTIC_v0_4_2.ipynb`; **die Oberfläche zeigt v0.5 – Entwurf**.

## 1. Einstieg

- [ ] Die frühere lange Versionenhistorie oben und unten fehlt. Sie ist in [CHANGELOG.md](../CHANGELOG.md) archiviert.
- [ ] Bei Modul **Isomerie** steht eine Auswahl der **sieben Isomerenpaare** im Vordergrund.
- [ ] Das erste Paar wird automatisch als Vergleich gezeigt; anschließend genügt ein Wechsel im Paar-Dropdown.
- [ ] Die optionale Einzelanalyse ist erst sichtbar, wenn „Optional: Einzelmolekül oder eigene SMILES untersuchen“ aktiviert wird.
- [ ] **Polarität und Löslichkeit**, **Funktionelle Gruppen**, **Konformere** und **Wirkstoffe und Biomoleküle** behalten ihren bisherigen Einzelmolekül-Workflow.

## 2. Die zentrale Vergleichsansicht

- [ ] Beide **2D-Strukturen** sind ohne Scrollen durch zwei große 3D-Karten erkennbar.
- [ ] Unter den Strukturen folgt **eine** gemeinsame Tabelle mit drei Spalten: Merkmal, Isomer A, Isomer B.
- [ ] Die Abschnitte heißen „Struktur und funktionelle Gruppen“, „Experimentelle / kuratierte Stoffdaten“ und „Qualitative Reaktivität“.
- [ ] Es gibt keine Pandas-Zeilenindizes (`0,1,...`).
- [ ] Die bislang verstreuten Stoffdaten und Reaktivitätshinweise sind dort enthalten, wo die Quelle entsprechende Einträge hat.
- [ ] Fehlende Werte stehen ausdrücklich als **„nicht hinterlegt“**, nicht als `0`.
- [ ] RDKit-Modellgrößen (TPSA, Crippen-logP, Rotationsdeskriptor) stehen in einem **aufklappbaren** Bereich.
- [ ] Der **nicht validierte** „Didaktische Polaritätseindruck“ und die heuristische „Wasserlöslichkeits-Tendenz“ werden im Isomerievergleich **nicht als Stoffeigenschaften** dargestellt.

## 3. Propanal / Aceton – fachliche Referenz

- [ ] Summenformel: **C₃H₆O / C₃H₆O**.
- [ ] Aldehyd / Keton sowie Bindungsumgebung des Carbonyl-C sind verständlich herausgearbeitet.
- [ ] Siedepunkt: **48–49 °C / 56,1 °C** aus vorhandenen kuratierten Daten.
- [ ] Wasserlöslichkeit: Propanal **gut, aber nicht vollständig mischbar** / Aceton **vollständig mischbar** (aus bestehenden Stoffdaten).
- [ ] Unter „Modellwerte“: **TPSA 17,07 / 17,07 Å²**, **Crippen-logP 0,60 / 0,60** und **rotierbare Bindungen (RDKit) 1 / 0**.
- [ ] Hinweis, dass **identische Modellwerte** keine identischen experimentellen Daten belegen.
- [ ] Die *experimentellen* log Kₒw-Werte sind **noch nicht** Teil der JSON-Datenbasis und wurden deshalb bewusst **nicht** als neue Messwerte in die App eingefügt.

## 4. 3D und andere Funktionen

- [ ] Bei Auswahl des Paares werden **nicht** sofort zwei 3D-Modelle erzeugt.
- [ ] „3D-Modell anzeigen“ erzeugt genau **eine** 3D-Ansicht.
- [ ] Mit dem Umschalter Propanal/Aceton wird die bestehende 3D-Ansicht ersetzt. Kein Überlaufen des Colab-Ausgabebereichs.
- [ ] Bei „Einzelmolekül untersuchen“ ist die bisherige detaillierte 2D-/3D-/Eigenschaften-Analyse weiterhin erreichbar.
- [ ] Die vier anderen Lernmodule und deren MC-/Konformerfunktionen sind unverändert bedienbar.
- [ ] Die Auswahl einer richtigen und falschen MC-Antwort führt zum korrekten Feedback; die Antwortoptionen sind gemischt.
- [ ] „SchülerInnen-Protokolltext erzeugen“ verwendet das aktive Isomerenpaar und enthält keine vermeintlichen experimentellen Polaritäts-Scores.

## 5. Sieben Paarungen nacheinander

1. Ethanol ↔ Dimethylether – H-Brücken, Siedepunkt
2. Propanal ↔ Aceton – Aldehyd/Keton
3. Butan ↔ Isobutan – Verzweigung; fehlende Stoffdaten sichtbar
4. Propansäure ↔ Essigsäuremethylester – Carbonsäure/Ester; Datenlücken sichtbar
5. D-Alanin ↔ L-Alanin – **Stereochemie erhalten**, kein vermeintlicher einfacher Drehtrick
6. Glucose (offene Form) ↔ Fructose (offene Form) – Aldose/Ketose; **keine** isolierten Reinstoffdaten der offenen Konformation vortäuschen
7. Maleinsäure ↔ Fumarsäure – cis/trans, Schmelz-/Löslichkeitsunterschiede, SMILES-Stereochemie

## Automatische Regression (im Entwicklungszweig)

```bash
python3 tests/validate_notebook.py
python3 tests/descriptor_regression.py
python3 tests/isomer_interface_regression.py
```

Dabei werden der Notebook-Python-Code, 61 Einzelkarten, sieben Isomerenpaar-Quizzes, sieben Paarvergleiche, Modellwerte, 3D-Lazy-Loading, Reports und die Modul-Umschaltung geprüft. Die integrierten Tests sind im GitHub-Actions-Workflow hinterlegt.

**Abnahmeentscheidung:** Erst nach positivem Colab-Praxistest das Notebook auf `main` übernehmen und **anschließend** die Anleitung der MOLEKÜL-WERKSTATT bei MW-001 und MW-009 auf den neuen Paar-Dropdown umstellen. Bis dahin laufen die bekannten Links und Aufgaben unverändert.
