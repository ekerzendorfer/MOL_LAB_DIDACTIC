# MOL_LAB DIDACTIC v0.3.4

Didaktische Molekülwerkstatt für den Chemieunterricht der SEK2.

[![In Colab öffnen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_3_4.ipynb)

## Ziel

MOL_LAB DIDACTIC hilft SchülerInnen, aus Molekülstruktur, räumlicher Gestalt, funktionellen Gruppen und einfachen Modellwerten auf Stoffeigenschaften zu schließen.

Die App ist bewusst **keine Moleküldatenbank** und keine Scientific-Version. Stoffdaten und spätere Reaktivitäts-Hinweise dienen immer der Deutung des Molekülbaus.

## Dateien

```text
MOL_LAB_DIDACTIC_v0_3_4.ipynb
molecules_v0_3_4.json
README.md
```

## Neu in v0.3.4

- JSON-Struktur vereinheitlicht:
  - `meta`
  - `modules`
  - `isomer_pairs`
  - `polarity_pairs`
  - vorbereitete `future_datasets`
- Alternative JSON-Datenpakete sind vorbereitet, aber noch nicht als sichtbare UI-Funktion aktiviert.
- In den Moleküleinträgen sind Felder für `stoffdaten` vorbereitet.
- In den Moleküleinträgen sind Felder für spätere qualitative `reaktivitaet` vorbereitet:
  - Hinweis
  - Warum?
  - Reaktionsidee
- Multiple-Choice-Fragen wurden überarbeitet: Distraktoren bilden stärker typische Fehlvorstellungen ab.
- 3D-Rendering wurde gegenüber v0.3.3 nicht verändert, um die Stabilität zu erhalten.

## Didaktischer Schwerpunkt

Die wichtigsten Lernschritte bleiben:

1. Struktur betrachten
2. räumliche Form untersuchen
3. funktionelle Gruppen erkennen
4. Polarität und Wasserlöslichkeit qualitativ deuten
5. kuratierte Vergleichspaare nutzen, um Fehlvorstellungen aufzubrechen

## Hinweise zu Stoffdaten

Die Felder für Stoffdaten sind **kuratierte Unterrichtswerte**. Sie sind nur dort befüllt, wo sie didaktisch besonders nützlich sind, etwa bei Vergleichspaaren wie:

- Wasser / Schwefelwasserstoff
- Methan / Hexan
- Ethanol / 1-Hexanol
- Essigsäure / Palmitinsäure
- Maleinsäure / Fumarsäure

Die App berechnet weiterhin automatisch:

- Summenformel
- molare Masse
- H-Brücken-Donoren/-Akzeptoren
- logP
- TPSA
- Rotierbarkeit / Ringe / schwere Atome

## Reaktivitäts-Hinweise

Die JSON enthält vorbereitete Felder für eine spätere qualitative Reaktivitätsbox. Diese wird in v0.3.4 noch nicht angezeigt.

Geplanter Dreischritt:

```text
Reaktivitäts-Hinweis
Warum?
Reaktionsidee
```

Diese Hinweise sollen später keine vollständige Reaktionslehre ersetzen, sondern die chemische Bedeutung funktioneller Gruppen andeuten.

## Start in Colab

1. Dateien ins Root-Verzeichnis des GitHub-Repos legen.
2. Notebook über den Colab-Button öffnen.
3. In Colab: **Laufzeit → Alle ausführen**.

## Abgrenzung zu MOL_LAB Scientific

MOL_LAB DIDACTIC bleibt bewusst schlank:

- kein xTB
- keine exakte ESP-Oberfläche
- kein Docking
- keine komplexen Biomoleküle wie ATP oder Acetyl-CoA
- keine freie Moleküldatenbank

Für vertiefte quantenchemische Berechnungen bleibt die Scientific-Version zuständig.
