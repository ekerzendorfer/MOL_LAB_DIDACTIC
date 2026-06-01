# MOL_LAB DIDACTIC

**MOL_LAB DIDACTIC** ist eine didaktisch reduzierte Molekülwerkstatt für den Chemieunterricht in der SEK 2.  
Das Tool soll SchülerInnen dabei unterstützen, aus der **Struktur kleiner Moleküle** auf **Stoffeigenschaften** zu schließen.

Im Mittelpunkt stehen nicht möglichst viele Rechenoptionen, sondern geführte Lernmodule zu:

- Polarität und Löslichkeit
- Isomerie
- funktionellen Gruppen
- Konformeren
- Wirkstoffen und Biomolekülen

Die App läuft als Google-Colab-Notebook und verwendet im Hintergrund **RDKit**, **py3Dmol**, **ipywidgets** und **pandas**.  
Es werden keine xTB-, CREST- oder Docking-Installationen benötigt.

---

## In Colab öffnen

[![In Colab öffnen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_1.ipynb)

Nach dem Öffnen in Colab:

1. **Laufzeit → Alle ausführen** wählen.
2. Warten, bis die Installation abgeschlossen ist.
3. Die interaktive Oberfläche im Notebook verwenden.

---

## Zielgruppe

Das Notebook ist gedacht für:

- SchülerInnen der SEK 2
- Chemieunterricht, Wahlpflichtfach, Laborzweige und NAWI-Unterricht
- LehrerInnenfortbildung
- niederschwellige Einführung in Struktur–Eigenschaft-Beziehungen

Es ist **nicht** als Forschungswerkzeug für professionelle Computational Chemistry gedacht.  
Die große Version mit erweiterten Rechenoptionen bleibt unabhängig davon im Projekt **MOL_LAB**.

---

## Didaktische Grundidee

Chemieunterricht versucht immer wieder, von den Eigenschaften kleinster Teilchen auf die Eigenschaften makroskopischer Stoffe zu schließen.

MOL_LAB DIDACTIC unterstützt diesen Weg:

```text
Molekülstruktur → Geometrie → funktionelle Gruppen → Polarität → Wechselwirkungen → Stoffeigenschaften
```

Die Lernenden sollen Moleküle nicht nur betrachten, sondern gezielt untersuchen:

1. **Beobachten**  
   Welche Strukturmerkmale sind sichtbar?

2. **Vermuten**  
   Welche Eigenschaft könnte sich daraus ergeben?

3. **Antwort prüfen**  
   Multiple-Choice-Fragen greifen typische Fehlvorstellungen auf.

4. **Erklärung anzeigen**  
   Eine kurze fachliche Erklärung verbindet Struktur und Eigenschaft.

5. **Modellgrenze beachten**  
   Berechnete Werte erklären Trends, ersetzen aber keine Experimente.

---

## Enthaltene Module in Version 0.1

### 1. Polarität und Löslichkeit

Beispiele:

- Wasser
- Methan
- Ammoniak
- Kohlenstoffdioxid
- Methanol
- Ethanol
- n-Butanol
- Methanal
- Aceton
- Diethylether
- Essigsäure

Zentrale Fragen:

- Wann ist ein Molekül polar?
- Warum führen polare Bindungen nicht automatisch zu einem polaren Molekül?
- Welche Rolle spielen Wasserstoffbrücken?
- Warum nimmt die Wasserlöslichkeit bei längeren Alkoholen ab?

---

### 2. Isomerie

Beispiele:

- Ethanol / Dimethylether
- Propanal / Aceton
- Butan / Isobutan
- Propansäure / Essigsäuremethylester
- Glucose / Fructose als Vertiefung
- D-Alanin / L-Alanin als Vertiefung zur Chiralität

Zentrale Fragen:

- Warum reicht die Summenformel nicht aus?
- Wie beeinflusst die Verknüpfung der Atome die Eigenschaften?
- Was unterscheidet Konstitutionsisomerie von Chiralität?

---

### 3. Funktionelle Gruppen

Beispiele:

- Methanol
- Ethanal
- Aceton
- Essigsäure
- Ethylacetat
- Diethylether
- Acetanhydrid
- Ethylamin
- Acetamid
- Phenol
- Anilin

Erkannt werden unter anderem:

- Alkohol
- Aldehyd
- Keton
- Carbonsäure
- Ester
- Ether
- Carbonsäureanhydrid
- Amin
- Amid
- Phenol
- Aromat

---

### 4. Konformere

Beispiele:

- Butan
- 1,2-Dichlorethan
- Ethylenglykol
- Cyclohexan
- Milchsäure

Das Modul erzeugt mehrere 3D-Konformere mit RDKit, optimiert sie mit MMFF/UFF und zeigt relative Energien der günstigsten Konformere.

Zentrale Fragen:

- Warum besitzt ein Molekül nicht immer nur eine räumliche Form?
- Welche Konformere sind energetisch günstiger?
- Was bedeutet Molekülbeweglichkeit für Stoffeigenschaften?

---

### 5. Wirkstoffe und Biomoleküle

Beispiele:

- Coffein
- Aspirin
- Paracetamol
- Ibuprofen
- Acetazolamid
- Glycin
- Alanin
- Phenylalanin
- Adenin
- Ribose

Zentrale Fragen:

- Welche funktionellen Gruppen besitzen bekannte Wirkstoffe?
- Wo liegen polare und unpolare Molekülbereiche?
- Welche Strukturmerkmale ermöglichen Wechselwirkungen mit Wasser oder Proteinen?
- Wie verbindet sich die Chemie kleiner Moleküle mit Biochemie?

---

## Berechnete und angezeigte Eigenschaften

MOL_LAB DIDACTIC berechnet einfache molekulare Kenngrößen mit RDKit:

| Eigenschaft | Bedeutung im Unterricht |
|---|---|
| Summenformel | Verbindung zwischen Strukturformel und Stoffebene |
| Molmasse | Bezug zu Stoffmenge und Molekülgröße |
| H-Brücken-Donoren | Fähigkeit, Wasserstoffbrücken zu spenden |
| H-Brücken-Akzeptoren | Fähigkeit, Wasserstoffbrücken aufzunehmen |
| logP | grobe Abschätzung hydrophiler/lipophiler Eigenschaften |
| TPSA | polare Oberfläche des Moleküls |
| rotierbare Bindungen | Beweglichkeit/Flexibilität |
| Ringanzahl | Starrheit und Ringsysteme |
| schwere Atome | Molekülgröße ohne Wasserstoffatome |
| funktionelle Gruppen | Struktur–Eigenschaft-Bezug in der organischen Chemie |

Wichtig: Diese Werte sind **Modellgrößen**. Sie erklären Trends, ersetzen aber keine experimentellen Messwerte.

---

## Eigene Moleküle untersuchen

Neben den vorbereiteten Beispielen können eigene Moleküle über einen **SMILES-Code** eingegeben werden.

Geeignet sind kleine bis mittelkleine Moleküle.  
Sehr große, salzartige, metallorganische oder ungewöhnlich komplexe Strukturen können fehlerhaft dargestellt oder nicht sinnvoll optimiert werden.

Beispiele für einfache SMILES-Codes:

```text
Ethanol:        CCO
Aceton:         CC(=O)C
Essigsäure:     CC(=O)O
Benzol:         c1ccccc1
Coffein:        Cn1cnc2n(C)c(=O)n(C)c(=O)c12
```

---

## Dateien im Repository

```text
MOL_LAB_DIDACTIC/
│
├── MOL_LAB_DIDACTIC_v0_1.ipynb   # Colab-Notebook
├── molecules_v0_1.json           # Moleküldatenbank mit didaktischen Karten
└── README.md                     # Projektbeschreibung
```

Die JSON-Datei muss im Repository neben dem Notebook liegen.

---

## Hinweis zur Verwendung im Unterricht

Empfohlener Ablauf:

1. Lehrkraft öffnet das Notebook in Colab.
2. **Laufzeit → Alle ausführen**.
3. Lernmodul auswählen.
4. Beispielmolekül auswählen.
5. SchülerInnen bearbeiten Beobachtungsfragen.
6. Multiple-Choice-Frage beantworten.
7. Erklärung und Modellgrenze diskutieren.
8. Optional: eigenes Molekül per SMILES untersuchen.

Besonders gut geeignet ist die Arbeit mit Molekülpaaren:

- Ethanol vs. Dimethylether
- Methanol vs. n-Butanol
- Propanal vs. Aceton
- Glucose vs. Fructose
- D-Alanin vs. L-Alanin

---

## Abgrenzung zu MOL_LAB

**MOL_LAB DIDACTIC** ist bewusst reduziert.

Nicht enthalten in Version 0.1:

- xTB-Rechnungen
- CREST-Konformersuche
- elektrostatische Oberflächen auf xTB-Basis
- Protein-Docking
- Proteinstrukturvorhersage
- externe KI-APIs

Diese Reduktion ist beabsichtigt: Das Notebook soll stabil, schnell und unmittelbar im Unterricht einsetzbar bleiben.

---

## Geplante Erweiterungen

Mögliche nächste Schritte:

- einklappbare LehrerInnenhinweise
- Export eines Kurzprotokolls als HTML/PDF/DOCX
- weitere kuratierte Molekülbeispiele
- Vergleichsansicht für Molekülpaare
- optionale experimentelle Daten zu Siedepunkt, Schmelzpunkt oder Löslichkeit
- zusätzliche Aufgabenserien
- GitHub-Pages-Startseite mit direktem Colab-Link

---

## Lizenz und Nutzung

Dieses Unterrichtswerkzeug ist als offenes Lehr-/Lernmaterial gedacht.  
Bitte bei Weiterverwendung die Quelle und das Repository angeben.

---

## Autor

Erich Kerzendorfer  
Projektkontext: **CHEMIE mit KI** / schulnahe digitale Werkzeuge für den Chemieunterricht
