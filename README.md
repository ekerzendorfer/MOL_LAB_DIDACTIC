# MOL_LAB DIDACTIC

**MOL_LAB DIDACTIC** ist eine bewusst reduzierte Molekülwerkstatt für den Chemieunterricht der SEK2.

Ziel ist nicht maximale Rechenchemie, sondern ein geführter didaktischer Zugang:

> Von Molekülstruktur und funktionellen Gruppen zu Stoffeigenschaften schließen.

## In Colab öffnen

[![In Colab öffnen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_1_1.ipynb)

## Version 0.1.1

Diese Version enthält gegenüber v0.1:

- robustere 3D-Darstellung in Google Colab
- Umschaltung zwischen **Kugel-Stab**, **Stabmodell** und **Kalottenmodell**
- technische Codezellen als Colab-Form-Zellen vorbereitet, damit der Code leichter ausgeblendet werden kann

## Zielgruppe

- SchülerInnen der SEK2
- Chemieunterricht, Laborzweige, Wahlpflicht, NAWI
- LehrerInnenfortbildung

## Module

1. **Polarität und Löslichkeit**  
   Wasser, Methan, Ammoniak, CO₂, Methanol, Ethanol, n-Butanol, Methanal, Aceton, Diethylether, Essigsäure

2. **Isomerie**  
   einfache Struktur- und Funktionsisomerie sowie Vertiefungen wie Glucose/Fructose und D-/L-Alanin

3. **Funktionelle Gruppen**  
   Alkohol, Aldehyd, Keton, Carbonsäure, Ester, Ether, Anhydrid, Amin, Amid, Phenol, Anilin

4. **Konformere**  
   einfache RDKit/MMFF-Konformersuche für kleine Moleküle

5. **Wirkstoffe und Biomoleküle**  
   Coffein, Aspirin, Paracetamol, Ibuprofen, Acetazolamid, Aminosäuren und kleine Biomoleküle

## Didaktischer Ablauf

Jedes Beispiel folgt dem Schema:

1. **Leitfrage**
2. **Beobachte**
3. **Vermute**
4. **Antwort prüfen**
5. **Erklärung anzeigen**
6. **Modellgrenze**

Damit sollen SchülerInnen nicht nur Moleküle ansehen, sondern aktiv Strukturmerkmale mit Eigenschaften verknüpfen.

## Technischer Kern

- RDKit
- py3Dmol
- ipywidgets
- pandas

Bewusst nicht enthalten:

- xTB
- CREST
- Docking
- Proteinstrukturvorhersage
- externe KI-API

Diese fortgeschrittenen Funktionen bleiben dem großen MOL_LAB vorbehalten.

## Repo-Struktur

```text
MOL_LAB_DIDACTIC/
├── MOL_LAB_DIDACTIC_v0_1_1.ipynb
├── molecules_v0_1.json
└── README.md
```

## Start in Colab

1. Notebook über den Colab-Button öffnen.
2. In Colab: **Laufzeit → Alle ausführen**.
3. Das Notebook installiert die benötigten Pakete und zeigt danach die Bedienoberfläche.
4. Technische Codezellen können in Colab über **Code anzeigen/ausblenden** eingeklappt werden.

## Hinweis zur SMILES-Eingabe

Eigene SMILES-Codes sind erlaubt, aber die App ist für kleine bis mittelkleine Moleküle gedacht. Große, geladene oder ungewöhnliche Strukturen können mit diesem einfachen Modell nur eingeschränkt sinnvoll analysiert werden.

## Geplante Erweiterungen

- einklappbare LehrerInnenhinweise
- kuratierte experimentelle Vergleichsdaten
- besserer Berichtsexport
- zusätzliche Arbeitskarten
- weitere Beispielsets
