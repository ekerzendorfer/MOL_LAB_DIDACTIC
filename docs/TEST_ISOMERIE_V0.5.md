# DIDACTIC v0.5 – Abnahme der neuen Isomerie-Ansicht

**Stand:** 24.11.2026 · **Entwicklungszweig:** `v0.5-isomerien-vergleich`  
**Status:** Automatische Chemie-, Daten-, Notebook- und Widgettests erfolgreich. **Erneuter visueller Colab-Test der neuesten Nachbesserungen steht noch aus.** Die stabile `main`-Version bleibt unverändert.

## Isolierter Test in Colab

- [Entwicklungsnotebook direkt in Colab öffnen](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/v0.5-isomerien-vergleich/MOL_LAB_DIDACTIC_v0_4_2.ipynb)
- Alternativ die [Notebook-Datei auf dem Entwicklungszweig](https://github.com/ekerzendorfer/MOL_LAB_DIDACTIC/blob/v0.5-isomerien-vergleich/MOL_LAB_DIDACTIC_v0_4_2.ipynb) öffnen.
- **Laufzeit → Alle ausführen**. Keine Ausführung in einer älteren, noch aktiven Laufzeit voraussetzen.

Der Dateiname bleibt aus Kompatibilitätsgründen `MOL_LAB_DIDACTIC_v0_4_2.ipynb`; **die Oberfläche zeigt v0.5 – Entwurf**.

## 1. Einstieg

- [ ] Die frühere lange Versionenhistorie oben und unten fehlt. Sie ist in [CHANGELOG.md](../CHANGELOG.md) archiviert.
- [ ] Bei Modul **Isomerie** steht eine Auswahl der **sieben Isomerenpaare** im Vordergrund.
- [ ] Beim Öffnen von **Isomerie** erscheint **noch kein Paar**; zuerst bewusst ein Paar wählen. **Diese Auswahl startet den Vergleich sofort**; ein zusätzlicher Button ist nicht mehr nötig.
- [ ] Die optionale Einzelanalyse ist erst sichtbar, wenn „Optional: Einzelmolekül oder eigene SMILES untersuchen“ aktiviert wird.
- [ ] **Polarität und Löslichkeit**, **Funktionelle Gruppen**, **Konformere** und **Wirkstoffe und Biomoleküle** behalten ihren bisherigen Einzelmolekül-Workflow.

## 2. Die zentrale Vergleichsansicht

- [ ] Beide **2D-Strukturen** sind ohne Scrollen durch zwei große 3D-Karten erkennbar.
- [ ] Unter den Strukturen folgt **eine** gemeinsame Tabelle mit drei Spalten: Merkmal, Isomer A, Isomer B.
- [ ] Die Abschnitte heißen „Struktur und funktionelle Gruppen“, „Experimentelle / kuratierte Stoffdaten“ und „Qualitative Reaktivität“.
- [ ] Es gibt keine Pandas-Zeilenindizes (`0,1,...`).
- [ ] Die bislang verstreuten Stoffdaten und Reaktivitätshinweise sind dort enthalten, wo die Quelle entsprechende Einträge hat.
- [ ] Leere Datenfelder werden nicht als viele einzelne Tabellenzeilen angezeigt. Bei gänzlich fehlenden Stoffdaten erscheint nur ein kurzer Hinweis; einzelne fehlende Gegenwerte stehen als **„nicht hinterlegt“**, niemals `0`.
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
- [ ] **Direkt an jeder kompakten Strukturkarte** zwischen **2D**, **3D** und **„Oberfläche (qualitativ)“** wechseln; 2D und 3D sind gleich breit; der 3D-Aufbau erfolgt nur bei Bedarf.
- [ ] Der 3D-Inhalt ersetzt jeweils **das 2D-Bild derselben Struktur**. Beide Karten lassen sich unabhängig umschalten. Die Oberfläche zeigt elementgefärbte Van-der-Waals-Flächen, **kein** quantitatives elektrostatisches Potential.
- [ ] Bei „Einzelmolekül untersuchen“ ist die bisherige detaillierte 2D-/3D-/Eigenschaften-Analyse weiterhin erreichbar.
- [ ] Die vier anderen Lernmodule und deren MC-/Konformerfunktionen sind unverändert bedienbar.
- [ ] Die vier MC-Antworten stehen in **vier separat anklickbaren, mehrzeiligen Auswahlzeilen**, ohne überlappende Beschriftung und ohne vorausgewählte Antwort. „Antwort prüfen“ ohne Auswahl zeigt **direkt unter den Schaltflächen** eine Aufforderung. Eine richtige bzw. falsche Antwort zeigt Feedback an derselben Stelle, ebenso „Erklärung anzeigen“. Die Antwortoptionen sind gemischt.
- [ ] „SchülerInnen-Protokolltext erzeugen“ verwendet das aktive Isomerenpaar und enthält keine vermeintlichen experimentellen Polaritäts-Scores.

## 5. Sieben Paarungen nacheinander

1. Ethanol ↔ Dimethylether – H-Brücken, Siedepunkt
2. Propanal ↔ Aceton – Aldehyd/Keton
3. Butan ↔ Isobutan – Verzweigung; **neue quellenbelegte Werte** ca. −0,5/−12 °C Siedepunkt und −138/−160 °C Schmelzpunkt; Löslichkeit beider Stoffe sehr gering
4. Propansäure ↔ Essigsäuremethylester – Säure/Ester; **neu ergänzt** Schmelzpunkte ca. −21/−98 °C, Siedepunkte 141/57 °C, deutlich verschiedene Wasserlöslichkeit
5. D-Alanin ↔ L-Alanin – **Stereochemie erhalten**, keine freie Rotation als Spiegelung. Keine fingierten experimentellen Unterschiede achiraler Stoffwerte.
6. Glucose (offene Form) ↔ Fructose (offene Form) – Aldose/Ketose; **keine** isolierten Reinstoffdaten der offenen Form vortäuschen; vorhandene offene SMILES spezifizieren die Stereozentren nicht.
7. Maleinsäure ↔ Fumarsäure – cis/trans, Schmelz-/Löslichkeitsunterschiede, SMILES-Stereochemie

## Automatische Regression (im Entwicklungszweig)

```bash
python3 tests/validate_notebook.py
python3 tests/descriptor_regression.py
python3 tests/isomer_interface_regression.py
```

Dabei werden der Notebook-Python-Code, 61 Einzelkarten, sieben Isomerenpaar-Quizzes, sieben Paarvergleiche, Modellwerte, 3D-Lazy-Loading, Reports und die Modul-Umschaltung geprüft. Die integrierten Tests sind im GitHub-Actions-Workflow hinterlegt.

**Abnahmeentscheidung:** Erst nach positivem Colab-Praxistest das Notebook auf `main` übernehmen und **anschließend** die Anleitung der MOLEKÜL-WERKSTATT bei MW-001 und MW-009 auf den neuen Paar-Dropdown umstellen. Bis dahin laufen die bekannten Links und Aufgaben unverändert.

## V0.5-Nachbesserungen nach dem ersten Praxistest (24.11.2026)

- Kein automatischer Start mehr bei bloßer Modulauswahl; bewusst gewähltes Paar und expliziter Klick.
- Die **2D/3D/Oberflächen-Umschalter sitzen unmittelbar an beiden Strukturkarten**, die lange Tabelle darunter.
- Einfache Element-Oberfläche: **qualitatives Visualisieren**, keine berechnete elektrostatische Potentialfläche oder echte Lipophilie-Oberfläche.
- MC-Feedback erscheint in einem **live aktualisierten HTML-Widget direkt unter den Antwort-Buttons** statt im unsichtbar weit entfernten Feedback-Output.
- Quelle und Bedingungen sind bei den ergänzten Stoffdaten dokumentiert. Die Werte für Butan/Isobutan und Propansäure/Essigsäuremethylester werden in der Entwicklungs-JSON und zur Prüfung auch im Notebook-Fallback hinterlegt.
- Für strukturelle Fälle ohne belastbare isolierte Stoffwerte (D-/L-Alanin, offene Zucker) keine pauschalen Zahlen eingesetzt; lange Tabellen mit „nicht hinterlegt“ werden vermieden.

**Zusätzlich überprüfen:** Ob die neuen Notebook-internen 3D-Karten auch in einer frischen Google-Colab-Laufzeit zuverlässig zwischen Bild, Kugel-Stab-Modell und Elementoberfläche wechseln. Der Headless-Test kann die clientseitige Rendering-Engine nicht ersetzen.

## Bedienkorrekturen nach Colab-Screenshots (24.11.2026)

- Vier Antwortzeilen mit unabhängig umbrochenem HTML-Text und jeweils einer Checkbox (technisch gegenseitig ausschließend) ersetzen das fehleranfällige native Colab-RadioButtons-Layout. Der Platzhalter zählt nicht als fünfte Antwort.
- 2D, 3D und qualitative Oberfläche verwenden ein Anzeigefenster mit 410 px Breite (auf kleinen Bildschirmen maximal 100 %), die zwei Karten haben je 475 px Breite; die Vergleichstabelle bleibt bis 1040 px breit.
- Bei Auswahl eines Isomerenpaars startet die Auswertung direkt. Das Dropdown bleibt zunächst leer, wenn man nur das Modul Isomerie öffnet. Der separate Vergleichs-Button entfällt.
- Die automatischen UI-Tests prüfen Checkbox-Auswahl, automatische Paarumschaltung und Kartenbreite. Der visuelle Test direkt in Colab ist weiterhin notwendig.
