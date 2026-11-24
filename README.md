# MOL_LAB DIDACTIC v0.5

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
