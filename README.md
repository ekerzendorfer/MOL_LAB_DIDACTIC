# MOL_LAB DIDACTIC v0.3

Didaktische Molekülwerkstatt für den Chemieunterricht der SEK2.

[![In Colab öffnen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_3.ipynb)

## Ziel

MOL_LAB DIDACTIC hilft SchülerInnen, aus Molekülstruktur, räumlicher Gestalt und funktionellen Gruppen einfache Stoffeigenschaften abzuleiten.

Die App ist bewusst keine wissenschaftliche Vollversion. xTB, CREST, exakte ESP-Oberflächen und komplexe Biomoleküle bleiben der Scientific-Version beziehungsweise späteren Spezialtools vorbehalten.

## Neu in v0.3

- Modul **Polarität und Löslichkeit** mit kuratierten Vergleichspaaren
- Mini-Aufgaben zu typischen Fehlvorstellungen
- optionaler experimenteller Bezug bei ausgewählten Paaren
- direkte Schaltflächen für die vier 3D-Darstellungen:
  - Kugel-Stab
  - Stabmodell
  - Kalottenmodell
  - Didaktische Polaritätsoberfläche
- zusätzliche Beispiele wie Schwefelwasserstoff, Hexan, 1-Hexanol, Palmitinsäure, Diethylenglycol, Maleinsäure/Fumarsäure, Salicylsäure, Vanillin und Citronensäure

## Didaktische Vergleichspaare in Modul 1

- Wasser vs. Schwefelwasserstoff
- Methan vs. Hexan
- Ethanol vs. 1-Hexanol
- Essigsäure vs. Palmitinsäure
- Diethylether vs. Diethylenglycol
- Methanol vs. Methanal
- Aceton vs. Essigsäure

Diese Paare sind bewusst kuratiert. Es gibt vorerst keinen freien Vergleichsmodus, damit die Oberfläche klar bleibt und keine didaktisch unsinnigen Zufallsvergleiche entstehen.

## Installation und Start

In Colab: **Laufzeit → Alle ausführen**. Nach der Installation erscheint die Bedienoberfläche.

## Repo-Struktur

```text
MOL_LAB_DIDACTIC/
├── MOL_LAB_DIDACTIC_v0_3.ipynb
├── molecules_v0_3.json
└── README.md
```

Das Notebook enthält die Moleküldaten zusätzlich eingebettet, damit es in Colab möglichst robust startet.

## Hinweise

Die qualitativen Skalen für Polarität und Wasserlöslichkeit sind didaktische Näherungen. Sie kombinieren Modellwerte wie logP, TPSA, H-Brücken-Donoren/-Akzeptoren und Molekülgröße. Sie ersetzen keine experimentellen Stoffdaten.
