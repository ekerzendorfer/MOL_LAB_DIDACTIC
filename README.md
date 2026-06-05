# MOL_LAB DIDACTIC v0.3.2

Didaktische Molekülwerkstatt für den Chemieunterricht der SEK2.

[![In Colab öffnen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_3_2.ipynb)

## Ziel

MOL_LAB DIDACTIC hilft SchülerInnen, aus Molekülstruktur, räumlicher Gestalt und funktionellen Gruppen einfache Stoffeigenschaften abzuleiten.

Die App ist bewusst keine wissenschaftliche Vollversion. xTB, CREST, exakte ESP-Oberflächen und komplexe Biomoleküle bleiben der Scientific-Version beziehungsweise späteren Spezialtools vorbehalten.

## Neu in v0.3.2

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
├── MOL_LAB_DIDACTIC_v0_3_2.ipynb
├── molecules_v0_3.json
└── README.md
```

Das Notebook enthält die Moleküldaten zusätzlich eingebettet, damit es in Colab möglichst robust startet.

## Hinweise

Die qualitativen Skalen für Polarität und Wasserlöslichkeit sind didaktische Näherungen. Sie kombinieren Modellwerte wie logP, TPSA, H-Brücken-Donoren/-Akzeptoren und Molekülgröße. Sie ersetzen keine experimentellen Stoffdaten.


## Hinweis zu v0.3.2

Die 3D-Darstellung wurde gegenüber v0.3 wieder auf die stabile Dropdown-Auswahl zurückgestellt, weil die Schaltflächen-Variante in Colab bei manchen Tests leere 3D-Frames erzeugte.


## Änderungen in v0.3.2

- Layout im Modul **Polarität und Löslichkeit** verdichtet: Vergleichspaar-Auswahl und Vergleichsbutton stehen nebeneinander.
- Die Auswahl des Vergleichspaares wird zurückgesetzt, wenn ein neues Einzelbeispiel gewählt wird.
- Die Schaltfläche **3D-Anzeige neu aufbauen** steht direkt neben der 3D-Engine-Auswahl.
- Vor neuen 3D-Renderings werden alte 3D-Frames aggressiver aus dem Colab-Frontend entfernt, um WebGL-/Browser-Hänger zu reduzieren.

