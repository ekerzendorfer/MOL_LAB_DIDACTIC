# MOL_LAB DIDACTIC v0.8

**Molekülwerkstatt für den Chemieunterricht der SEK2**  
Didaktisch reduzierte Colab-App zur Untersuchung von Struktur, räumlicher Gestalt, Polarität, Löslichkeit, Isomerie, funktionellen Gruppen, Konformeren und einfachen Struktur–Eigenschafts-Beziehungen.

[![In Colab öffnen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_4_2.ipynb)

## Neu in V0.5 (24.11.2026)

- **Isomerie als direkter Paarvergleich:** sieben kuratierte Paare, Auswahl startet den Vergleich unmittelbar
- **Kompakte 2D/3D/Elementoberfläche** pro Molekül mit gleich breiten Anzeigeflächen, 3D-Berechnung erst bei Bedarf
- **Eine gemeinsame Vergleichstabelle**, experimentelle Stoffdaten getrennt von RDKit-Modellwerten und Quellbedingungen
- **MC-Antworten ohne Überlappung:** vier umbrechende Auswahlzeilen, Antwortprüfung und Erklärung
- RDKit-Deskriptoren für alle Einträge regressionsgeprüft; nicht validierte heuristische Polaritäts-/Löslichkeitsscores im Isomerievergleich entfernt

Die Colab-Oberfläche für Isomerie wurde vom Anwender geprüft und am 24.11.2026 freigegeben. Die anderen Module werden gesondert fachlich durchgesehen. Dateinamen `MOL_LAB_DIDACTIC_v0_4_2.ipynb` und `molecules_v0_4_2.json` bleiben zur Wahrung bestehender Links unverändert.

## Historie: Neu in v0.4.2

- **SchülerInnen-Protokolltext** über eine einzige Schaltfläche
- **Reaktivitäts-Hinweise** als aufklappbare Dreischritt-Erklärung: *Hinweis – Warum? – Reaktionsidee*
- **Stoffdaten / experimenteller Bezug** in kuratierten Molekülvergleichen und Isomerenvergleichen
- JSON-Struktur weiter stabilisiert; alternative Niveaustufen und ein späterer Editor bleiben vorbereitet
- 3D-Rendering bleibt bewusst unverändert gegenüber v0.3.4, um die Stabilität zu erhalten

## Dateien

```text
MOL_LAB_DIDACTIC_v0_4_2.ipynb
molecules_v0_4_2.json
README.md
```

Alle Dateien sollten im Root-Verzeichnis des Repos liegen.

## Start in Google Colab

```text
https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_4_2.ipynb
```

In Colab anschließend: **Laufzeit → Alle ausführen**.

## Didaktisches Prinzip

MOL_LAB DIDACTIC ist kein Molekülkatalog und keine wissenschaftliche Datenbank. Die Beispiele sind kuratiert und sollen typische Fehlvorstellungen aufbrechen, etwa:

- gleiche Summenformel bedeutet nicht gleiche Stoffeigenschaft,
- polare Bindungen bedeuten nicht automatisch polares Molekül,
- eine polare funktionelle Gruppe garantiert keine gute Wasserlöslichkeit,
- kleine Strukturunterschiede können physikalische Eigenschaften und Reaktivität stark verändern.

## Grenzen

Die angezeigten Werte sind Modellwerte oder kuratierte Unterrichtsdaten. Reaktivitäts-Hinweise sind qualitative Orientierung anhand funktioneller Gruppen und ersetzen keine vollständige Reaktionslehre.


## Änderungen in v0.4.2

- Multiple-Choice-Fragen markieren nicht mehr automatisch die erste Antwort.
- Antwortprüfung ist gegen Vergleichsberichte abgesichert.
- Kleine Start-/UI-Korrekturen für die Antwortprüfung.


## Änderungen in v0.4.2

- Feinschliff der Multiple-Choice-Fragen: plausiblere Distraktoren statt offensichtlich falscher Antworten.
- Reaktivitäts-Hinweise textlich vereinheitlicht: Hinweis – Warum? – Reaktionsidee.
- Konformer-Modul um **n-Pentan** und **2-Butanol** ergänzt.
- JSON-Metadaten für spätere einklappbare Bereiche vorbereitet, ohne die Oberfläche zu verändern.
- Plus-Beispiele bleiben bewusst noch zurückgestellt.


## Datenkorrektur 23.11.2026 – Isomerie-Vergleich Ethanol/Dimethylether

Die bislang leeren Stoffdaten- und Reaktivitätsfelder für Dimethylether sind ergänzt. Die Dichte ist ausdrücklich als **Flüssigkeitsdichte unter Druck** gekennzeichnet. Datenquellen: PubChem CID 8254, NIST Chemistry WebBook, FSANZ A1062.

Nach einem GitHub-Update in einer bereits laufenden Colab-Sitzung die Zelle **„MOL_LAB DIDACTIC starten“ erneut ausführen**, um die aktuelle JSON einzulesen; sofern nötig „Laufzeit → Neu starten“ und die Zellen erneut ausführen. Die Vergleichsroutine wurde nicht verändert.

## Qualitätsprüfung der Vergleichsaufgaben (November 2026)

Die Daten und Antwortprüfung wurden für die MOLEKÜL-WERKSTATT überarbeitet: Propanal-Stoffdaten/Reaktivität ergänzt, Multiple-Choice bei den Isomeren- und Polaritätsvergleichen aktiviert und die Antwortreihenfolge variiert. Beim ursprünglichen V0.4.2-Stand waren weitere `35` von `61` Molekül-Einträgen ohne Stoffdaten; manche (z. B. „Glucose offen“) sind bewusst Strukturmodelle und dürfen nicht mit Reinstoffdaten verwechselt werden.

Die vollständige Aufstellung und Reihenfolge für die spätere fachliche Feinarbeit steht unter [Datenqualität-Audit](docs/DATENQUALITAET_AUDIT_2026-11-23.md).

## V0.5 – Isomerie auf Paarvergleich umgestellt (freigegeben auf main)

Die neue Isomerie-Oberfläche ist nach dem Colab-Praxistest auf **`main` als V0.5 veröffentlicht**. Der bisherige Entwicklungszweig [`v0.5-isomerien-vergleich`](https://github.com/ekerzendorfer/MOL_LAB_DIDACTIC/tree/v0.5-isomerien-vergleich) bleibt als Entwicklungshistorie bestehen.

**[V0.5 auf main in Colab öffnen](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_4_2.ipynb)**  
**[Test- und Abnahmeanleitung](docs/TEST_ISOMERIE_V0.5.md)**

- Isomerie beginnt mit einer **bewussten Auswahl** der sieben kuratierten Isomerenpaare; die Analyse startet erst über „Vergleich anzeigen“, nicht automatisch bei der Modulauswahl.
- Pro Paar zwei kompakte **2D-Strukturkarten** und **eine durchgehende Vergleichstabelle**: gemeinsame Strukturmerkmale, experimentelle/kuratierte Stoffdaten, qualitative Reaktivität.
- **Weitere Modellwerte** (topologische polare Oberfläche, Wildman–Crippen-logP, RDKit-Rotationszählung) werden erklärend und **aufklappbar** dargestellt.
- Nicht validierte didaktische Polaritäts-/Löslichkeits-Scores werden im Isomerievergleich **nicht mehr** als Stoffeigenschaft ausgegeben.
- Jede Isomerenkarte besitzt direkt über ihrer späteren Vergleichstabelle einen **2D | 3D | Oberfläche (qualitativ)**-Umschalter; die Moleküle werden erst bei Bedarf in 3D optimiert. Ein atomfarbiger Van-der-Waals-Mantel ist keine elektrostatische Potentialfläche.
- **Sieben paarbezogene MC-Fragen** mit direkt darunter sichtbarem Feedback und Erklärung sowie der bewährte Protokollmechanismus.
- Schüleransicht ohne Versionshistorie; bisherige Texte in [CHANGELOG.md](CHANGELOG.md) archiviert.
- Drei automatisierte Checks: `tests/validate_notebook.py`, `tests/descriptor_regression.py`, `tests/isomer_interface_regression.py`.

**Keine experimentellen log Kₒw-Werte wurden dazuerfunden.** Solche Werte benötigen dokumentierte Quellen, Temperatur-/Stoffformbedingungen und separate fachliche Abnahme. Die MOLEKÜL-WERKSTATT soll für MW-001 und MW-009 die neue Paarwahl ohne zusätzlichen Vergleichsbutton verwenden.

### Nachbesserungen V0.5 nach Praxistest vom 24.11.2026

Für die Isomerie-Paare **Butan/Isobutan** und **Propansäure/Essigsäuremethylester** wurden experimentelle Schmelz-/Siedepunkte und qualitative Löslichkeitsangaben aus ICSC-/Fachquellen ergänzt und mit Bedingungen bzw. Quellen-URLs versehen. Die anderen Paare werden **nicht** mit ungeprüften Reinstoffdaten aufgefüllt. Bei offenen Zuckerformen sind solche Angaben zum isolierten offenen Molekül nicht sinnvoll.

Die gemeinsame Vergleichstabelle blendet weitgehend leere Abschnitte aus; der thematische Strukturhinweis bleibt erhalten. Für fehlende Angaben wird nie „0“ erfunden. Die neue [Prüfliste V0.5](docs/TEST_ISOMERIE_V0.5.md) berücksichtigt die gemeldeten Colab-Probleme.

Die Isomerie-Oberfläche wurde am 24.11.2026 in Colab abgenommen und anschließend auf main freigegeben.

### UI-Nachbesserung nach Colab-Test (24.11.2026)

In V0.5 startet die Isomerie-Analyse bei der Auswahl eines kuratierten Paares (nicht schon beim Öffnen des Moduls). Vier korrekt umbrechende Antwortzeilen ersetzen die in Colab überlappenden langen Radio-Optionen. Die beiden schmalen Strukturkarten behalten beim Wechsel zwischen 2D, 3D und Oberfläche dieselbe Breite. Der Colab-Praxistest war erfolgreich; V0.5 ist nun auf `main` verfügbar.

## V0.6-Entwurf – Polarität und Löslichkeit (24.11.2026)

**V0.6 nach positivem Praxistest am 24.11.2026 auf `main` freigegeben.** Der Entwicklungszweig bleibt als Historie bestehen.

- Die sieben kuratierten Polaritätspaare beginnen nach bewusster Auswahl direkt; die Einzelanalyse bleibt für MW-015 und eigene SMILES erhalten.
- Zwei kompakte Karten verwenden denselben 2D/3D/qualitativen Elementoberflächen-Umschalter wie Isomerie. Erst bei Bedarf wird eine 3D-Modellgeometrie berechnet.
- Statt mehrerer verstreuter Tabellen stehen die kuratierten Stoffdaten und Reaktivität in einer gemeinsamen Vergleichstabelle. RDKit-Modellwerte sind aufklappbar, unvalidierte Polaritäts-/Löslichkeits-Scores fehlen bewusst in Paaransicht und Paarbericht.
- Die Elementoberfläche ist **keine** elektrostatische Potentialfläche, kein Dipolmodell und keine quantitative Polaritätsmessung.
- Kleine fachliche Korrekturen: Aldehyd-Erkennung einschließlich Methanal, Trennung Ester/Carbonsäureanhydrid und Butan-MC zur anti-/gauche-Konformation im Konformer-Modul.
- Bei der Einzelanalyse bleiben die bisherigen Funktionen erhalten; die didaktische Heuristik wird sichtbar als **unvalidiert** gekennzeichnet.

**[V0.6-Colab-Testnotebook](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/v0.6-polaritaet-qualitaet/MOL_LAB_DIDACTIC_v0_4_2.ipynb)** · Visueller Praxistest erfolgreich abgeschlossen.

### V0.6-Freigabe

Die Polaritäts- und Löslichkeitsvergleiche wurden mit allen drei Ansichten in Colab visuell geprüft und am 24.11.2026 freigegeben. Der stabile JSON-Pfad zeigt nun auf `main`; V0.6 erhält weiterhin die bestehenden Notebook-/JSON-Dateinamen, damit Links gültig bleiben.

## V0.7 – Feinschliff der restlichen Module (Entwurf, 24.11.2026)

**Ausschließlich im Branch [v0.7-feinschliff-restmodule](https://github.com/ekerzendorfer/MOL_LAB_DIDACTIC/tree/v0.7-feinschliff-restmodule)**. Die freigegebene V0.6 auf `main` bleibt unverändert.

- **Funktionelle Gruppen:** In der Einzelanalyse lässt sich eine erkannte funktionelle Gruppe gezielt in der RDKit-2D-Darstellung hervorheben. Für Aromaten werden alle Ringatome markiert. Ester und Ether werden nicht mehr verwechselt; 3D- und Modellwertdarstellung bleiben verfügbar.
- **Konformere:** Eindeutige geometrische Minima über Heavy-Atom-RMSD statt bloßer Energiestufen. Für Butan und 1,2-Dichlorethan werden Diederwinkel (anti/gauche) angezeigt. Relative Kraftfeldenergien sind nicht experimentelle Populationen und keine Aktivierungsbarrieren.
- **Wirkstoffe und Biomoleküle:** Fünf generische MC-Fragen fachlich präzisiert, bei Glycin/Alanin/Phenylalanin Zwitterionen, bei Ribose die offenkettige und nicht stereospezifizierte Modellform erläutert. Unvalidierte Polaritäts-/Löslichkeits-Scores werden außerhalb des Polaritätsmoduls nicht mehr als Eigenschaft im Bericht geführt.
- **MOL_LAB** als möglicher späterer Vertiefungslink: Auswahl geeigneter Modellvergleiche und Datenübergabe gesondert prüfen; noch keine automatische Kopplung.

[**V0.7-Testnotebook in Colab öffnen**](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/v0.7-feinschliff-restmodule/MOL_LAB_DIDACTIC_v0_4_2.ipynb). Bitte vor Freigabe die neuen 2D-Markierungen bei Vanillin/Salicylsäure, Konformere Butan/1,2-Dichlorethan und MC-Fragen bei Ibuprofen/Alanin testen.

### V0.7-Nachtrag: Funktionelle Gruppen in Wirkstoffen und Biomolekülen

Die aus dem Modul *Funktionelle Gruppen* bekannte interaktive Hervorhebung ist jetzt auch bei *Wirkstoffe und Biomoleküle* verfügbar. Die 3D-Darstellung und bisherigen Aufgaben bleiben erhalten. Das SMARTS-Muster **Sulfonamid** wurde für Acetazolamid ergänzt. Die automatische Regression kontrolliert die Markierung und ihre Rücksetzung.

### Fachliche Feinkorrekturen der Gruppenmarkierung (24.11.2026)

- **–COOH = Carboxylgruppe** (die Bezeichnung *Carbonsäure* bleibt für die Stoffklasse korrekt).
- Eine Carbonylgruppe wird **nicht zusätzlich** als eigene Gruppe angeboten, wenn sie Teil einer Carboxyl-, Ester-, Amid- oder Carbonsäureanhydridgruppe ist; freie Aldehyd-/Keton-Carbonyle bleiben ansteuerbar.
- Coffein: Beide **Ring-Carbonylgruppen (C=O)** werden nun erkannt und können gemeinsam markiert werden, obwohl RDKit die betreffenden Carbonylkohlenstoffe als aromatisch erkennt.
- Coffein und Adenin: Bei kondensierten aromatischen Ringen heißt die Auswahl jetzt **Aromatisches Ringsystem (RDKit)**; markiert werden die aromatischen Ringatome und Ringbindungen. Aromatizität und Ringcarbonyle schließen einander nicht aus.
- Alle Änderungen im V0.7-Branch, V0.6 auf main bleibt stabil.

## V0.8 – Stereochemie und Glucose (auf main veröffentlicht: 25.11.2026)

Ausgehend vom Entwicklungsbranch `v0.8-stereochemie-glucose` sind seit der Freigabe auf `main` zwei bestehende Isomerie-Paare stereochemisch aufgewertet; ein geführter Glucose-Lernweg ist zusätzlich verfügbar.

- **D-/L-Alanin**: das stereogene α-C ist in 2D markiert, tatsächliche RDKit-CIP-Konfigurationen R/S werden erläutert; D/L ist nicht mit R/S oder (+)/(−) gleichzusetzen.
- **Maleinsäure/Fumarsäure**: die E/Z-relevante Doppelbindung ist markiert; Z/E und cis/trans werden didaktisch eingeordnet.
- **Glucose:** ein eigener Button unter dem Isomerie-Dropdown startet vier Lernschritte (offene D-Glucose; Kette/α; Kette/β; α/β nebeneinander). Verwendet stereochemisch definierte SMILES aus PubChem, ohne die bisherigen 61 Moleküleinträge oder sieben Vergleichspaare zu ändern. Das C1 der Aldehydform, C5–O und das anomere C1 sind farblich hervorgehoben. Die drei Karten bieten bei Bedarf 3D und qualitative Elementoberfläche.
- **Gleichgewicht:** intramolekulare Halbacetalbildung ohne Wasserabspaltung; Mutarotation über Ringöffnung und -schluss. Dies ist ein diskreter Strukturvergleich, keine quantitative Reaktions-, Geschwindigkeits- oder Gleichgewichtssimulation.
- Der Glucose-Lernweg hat eine eigene MC-Aufgabe, Erklärung und einen Protokolltext. Das **Reset-3D** stellt den gewählten Lernschritt wieder her. Tests prüfen echte Stereokonfiguration, C1-Differenz und die UI-Wechsel.

[**V0.8 auf main in Colab öffnen**](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_4_2.ipynb). Der Entwicklungsbranch bleibt als Historie erhalten.

### Abschlussbeispiel V0.8: Atorvastatin (24.11.2026)

Als **62. Moleküleintrag** und **12. Wirkstoff/Biomolekül** ergänzt: die neutrale freie Atorvastatinsäure, [PubChem CID 60823](https://pubchem.ncbi.nlm.nih.gov/compound/60823). Mit stereochemisch definiertem SMILES: C₃₃H₃₅FN₂O₅, 558,65 g/mol, 41 Schweratome, vier Ringe, zwölf nach RDKit definiert rotierbare Bindungen und zwei R-Stereozentren (3R,5R).

Im bestehenden Modul sind Carboxylgruppe, OH-Gruppen, Amid, aromatisches Ringsystem und neu **Arylfluorid** markierbar; die 2D-Darstellung erhält für diese umfangreiche Struktur eine größere Fläche. Eine kompakte Komplexitätsübersicht, eine eigene MC-Aufgabe sowie Beobachtungsfragen gehören zur Karte. **Keine** Vorhersage von Bindeposen oder Arzneiwirkung: freie Säure und pharmazeutisches Calciumsalz unterscheiden sich, und ein einzelnes 3D-Kraftfeldminimum ist nur ein Modell. Keine frei erfundenen experimentellen Stoffdaten.

Fosravuconazol ist weiterhin **nur als mögliche spätere Vertiefung** dokumentiert. V0.8 ist seit 25.11.2026 auf `main` freigegeben; vor einer öffentlichen Vorführung bleibt ein abschließender visueller Colab-Check sinnvoll.

### Cyclohexan: vier kuratierte Referenzgeometrien für MW-024 (25.11.2026)

Im Modul **Konformere → Cyclohexan** zeigt der Button **„Konformere berechnen“** vier gezielt erzeugte und mit RDKit/MMFF94 behandelte Ringformen nebeneinander: **Sessel, Twist-Boat, Wanne und Halbsessel**. Die Modellpotentiale folgen Sessel < Twist-Boat < Wanne < Halbsessel. Die Wanne ist eine **stationäre Sattel-/Übergangsgeometrie**, kein drittes stabiles Energieminimum. Aus mathematisch definierten Ring-Puckering-Startgeometrien werden H-Positionen und 3D-Geometrien mit zunächst festgehaltenen Ring-C-Atomen vorbereitet und dann im MMFF-Kraftfeld behandelt. Ring-Torsionen validieren die jeweils erzeugte Form.

Die dargestellten Energien sind **relative MMFF-Potentiale** (kcal/mol), weder experimentelle freie Energien noch Ringinversionsbarrieren. Literatur-Orientierung: Twist-Boat ~5,5 und Wanne ~6,9 kcal/mol über Sessel; modellabhängige Werte dürfen abweichen. Der Halbsessel ist ausdrücklich nur eine geometrisch eingeschränkte Annäherung, keine berechnete Übergangszustandsgeometrie. **Alle anderen Moleküle nutzen unverändert die bisherige ETKDG/MMFF-Minimasuche.** Die MW-024-Interaktion, Lernkontrolle, Protokoll und „3D neu aufbauen“ bleiben nutzbar.

Referenzen: [Oregon State University Cyclohexane Conformations](https://sites.science.oregonstate.edu/~gablek/CH334/Chapter4/bare_cyclohexane.htm), [Chemistry LibreTexts – Conformations of Cycloalkanes](https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Basic_Principles_of_Organic_Chemistry_%28Roberts_and_Caserio%29/12%3A_Cycloalkanes_Cycloalkenes_and_Cycloalkynes/12.03%3A_Conformations_of_Cycloalkanes).

### Ergänzung vom 25.11.2026: Halbsessel als vierte Ringreferenz

Cyclohexan zeigt nun **vier gezielte 3D-Ringformen**: Sessel, Twist-Boat, Wanne und Halbsessel (zwei Zeilen mit je zwei Referenzkarten bei ausreichender Fensterbreite). Die Vergleichstabelle enthält vier relative MMFF94-Potentialwerte. Die Ringinversion lässt sich als Sessel → Halbsessel → Twist-Boat → Wanne → Twist-Boat → Halbsessel → Sessel erklären.

**Wissenschaftliche Einordnung:** Die Wanne ist kein Energieminimum. Der Halbsessel ist in DIDACTIC ein **geometrisch eingeschränktes Referenzmodell** mit vier nahezu koplanaren Ring-C-Atomen und zwei benachbarten, entgegengesetzt ausgelenkten Ring-C-Atomen. Das MMFF-Potential wird an dieser restringierten Struktur ausgewertet, ohne einen Sattelpunkt per Hesse-/Frequenzanalyse zu lokalisieren. Die näherungsweise +10,8 kcal/mol für einen tatsächlichen Halbsessel-Übergangszustand sind nur eine **Literaturorientierung**, keine von DIDACTIC bestimmte Aktivierungsbarriere. Die freie Minimierung klappt die Halbsessel-Referenz zu einem Minimum zusammen. Andere Moleküle verwenden unverändert die allgemeine Konformersuche.

Literatur: [Carey & Sundberg, Advanced Organic Chemistry, Teil A, Stereochemistry/Conformation](https://beckassets.blob.core.windows.net/product/readingsample/436588/9780387448978_excerpt_001.pdf).

### Veröffentlichung von V0.8 auf main – 25.11.2026

Die stabile V0.8 bündelt die in V0.7 entwickelten funktionellen Gruppen/biochemischen Präzisierungen, stereochemische Isomerenpaare, den vierstufigen D-Glucose-Lernweg, Atorvastatin und den Cyclohexan-Vierervergleich einschließlich Halbsessel. Das Hauptnotebook liest seine JSON-Daten wieder aus `main`; Notebook- und JSON-Dateinamen bleiben zur Linkkompatibilität unverändert. Alle automatisierten Notebook-, RDKit-, UI- und didaktischen Regressionen wurden vor Veröffentlichung geprüft.

**Hinweis zur wissenschaftlichen Einordnung:** Die vier Cyclohexan-Bilder sind didaktische 3D-Referenzen, keine vier Minima. Die Halbsessel-Referenz nutzt geometrische Positionsrestriktionen, sodass ihre MMFF-Modellenergie nicht als gemessene oder präzise berechnete Barriere ausgegeben werden darf.

## V0.9a – Dipol-Lernmodus Wasser (Entwurf, 28.11.2026)

Nur auf `v0.9a-dipol-labor`. Modul **Polarität und Löslichkeit → Wasser → Molekül analysieren → Bindungsdipole untersuchen**. Drei Stufen im selben drehbaren 3D-Fenster: Geometrie, EN-Werte (Pauling), Bindungsdipole. Gleich lange qualitative Pfeile parallel zu den beiden O–H-Bindungen, H → O mit Querstrich am positiven Ende. Keine Debye-Werte; physikalische Dipolmomentkonvention entgegengesetzt. Die normale Einzelanalyse und alle anderen Module bleiben unverändert. Vektorsumme, CO₂, NH₃ und CH₄ folgen erst nach Colab-Abnahme. Die Metadaten halten das Basisset bereit, nur H₂O ist aktiv.

[Testanleitung V0.9a](docs/TEST_DIPOL_V0.9a.md).

## V0.9b – Räumliche Vektoraddition (Entwurf)

Abgenommene V0.9a bleibt separat erhalten. Wasser und CO₂ sind im Dipol-Lernmodus aktiv. Stufe 4 zeigt freie Vektoren (blau/orange), Spitze-an-Anfang-Konstruktion, grüne Resultierende bzw. Nullsumme und schließlich die Modellresultierende am Molekül. Vor-/Zurück ohne Neuladen des Viewers. CO₂ verwendet ausschließlich im Lernmodus eine idealisierte lineare, symmetrische Geometrie, um numerische Restpfeile zu vermeiden. Keine Debye-Werte. [Testanleitung](docs/TEST_DIPOL_V0.9b.md).
