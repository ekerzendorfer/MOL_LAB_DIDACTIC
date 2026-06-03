# MOL_LAB DIDACTIC

**MOL_LAB DIDACTIC** ist eine didaktisch reduzierte Molekülwerkstatt für den Chemieunterricht der SEK2.  
Ziel ist nicht maximale Forschungsnähe, sondern ein klarer Zugang von der Molekülstruktur zu Stoffeigenschaften.

[![In Colab öffnen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_2.ipynb)

## Version 0.2

Neu gegenüber v0.1.8:

- kompakte qualitative Skala **Didaktischer Polaritätseindruck**
- kompakte qualitative Skala **Wasserlöslichkeits-Tendenz**
- kurze automatische Begründung unter den berechneten Eigenschaften
- aufklappbarer Hinweis zu **Näherungen und Modellgrenzen**
- neuer 3D-Modus **Didaktische Polaritätsoberfläche**
- Rohwerte wie `logP` und `TPSA` bleiben weiterhin in der Tabelle sichtbar

Die beiden Skalen sind ausdrücklich **didaktische Näherungen**. Sie helfen, Trends zu verstehen, ersetzen aber keine experimentellen Stoffdaten.

## Zielgruppe

- SchülerInnen der SEK2
- Chemieunterricht, Laborzweige, Wahlpflichtfach, NAWI
- LehrerInnenfortbildung

## Module

1. **Polarität und Löslichkeit**
2. **Isomerie**
3. **Funktionelle Gruppen**
4. **Konformere**
5. **Wirkstoffe und Biomoleküle**

## Bedienung

1. Notebook in Google Colab öffnen.
2. `Laufzeit → Alle ausführen` wählen.
3. Lernmodul und Beispielmolekül auswählen.
4. Optional ein eigenes kleines Molekül als SMILES eingeben.
5. Analyse starten.

## Technischer Kern

- RDKit
- py3Dmol / 3Dmol.js
- ipywidgets
- pandas

Es wird bewusst kein xTB, kein CREST, kein Docking und keine externe KI-API verwendet.

## Dateien

```text
MOL_LAB_DIDACTIC/
├── MOL_LAB_DIDACTIC_v0_2.ipynb
├── molecules_v0_1.json
└── README.md
```

## Abgrenzung zu MOL_LAB

Das große **MOL_LAB** bleibt die wissenschaftlichere Version mit erweiterten Rechenmethoden.  
**MOL_LAB DIDACTIC** ist die schulnahe Version: weniger Optionen, mehr Führung, klarere didaktische Struktur.

## Lizenz / Nutzung

Für Unterricht und LehrerInnenfortbildung gedacht. Bitte fachlich prüfen, bevor Ergebnisse als experimentelle Stoffdaten verwendet werden.
