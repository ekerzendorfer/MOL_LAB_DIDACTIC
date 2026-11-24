# Konzept: Isomerie-Modul und Deskriptor-Qualität in MOL_LAB DIDACTIC

**Stand:** 24.11.2026 · **Status:** Vorschlag / noch nicht implementiert  
**Betroffene aktuelle Version:** `MOL_LAB_DIDACTIC_v0_4_2.ipynb` (v0.4.2)  
**Auslöser:** Praxistest MW-009 Propanal/Aceton; Rückmeldung zur Vergleichsansicht, Modellwerten und Notebooksichtbarkeit.  
**Geltung:** Zunächst *nur* das Modul „Isomerie“, gemeinsame Deskriptor-Funktionen werden jedoch für alle Module überprüft. Die bestehende Notebook-Funktionalität bleibt bis zur fachlichen Freigabe unverändert.

## 1. Diagnose im aktuellen Code

Die Descriptor-Funktion `calc_properties(mol)` verwendet gegenwärtig:

- `Crippen.MolLogP(mol)`: atombeitragsbasiertes Wildman–Crippen-**Vorhersagemodell**, kein gemessener Octanol/Wasser-Verteilungskoeffizient.
- `rdMolDescriptors.CalcTPSA(mol)`: **topologische** polare Oberfläche (Ertl-Fragmentbeiträge), kein 3D-Dipolmoment.
- `rdMolDescriptors.CalcNumRotatableBonds(mol)`: Rotationsfreiheiten **nach RDKit-Deskriptordefinition**, bei der u. a. Einfachbindungen zu endständigen Schweratomgruppen nicht mitgezählt werden.
- `qualitative_polarity_assessment(mol, props)`: **eigene**, heuristische Score-Bildung aus TPSA, vorhergesagtem logP, Donor-/Akzeptorzahl, Molekülgröße und Ladung. **Nicht** eine Messung der Molekülpolarität oder eine verlässliche Vorhersage der experimentellen Wasserlöslichkeit.

Die aktuelle Isomeren-Funktion `display_isomer_comparison(card_a, card_b)` erzeugt nacheinander zwei umfangreiche Strukturkarten (je 2D+3D), ein `pandas.DataFrame` mit durchnummeriertem Zeilenindex, einen separaten Stoffdaten-`<details>`-Block und einen separaten Reaktivitäts-`<details>`-Block. Dadurch verteilt sich der fachliche Vergleich über mehrere vertikale Bereiche; die Strukturkarten benötigen auf schmalen Bildschirmen sehr viel Höhe.

Das Notebook enthält zusätzlich Versions-/Entwicklungshinweise in der ersten Markdown-Zelle und in der letzten Markdown-Zelle. Diese sind für Schülerinnen und Schüler nicht erforderlich.

## 2. Nachrechnung als Regressionstest

Unabhängige RDKit-Nachrechnung mit **RDKit 2025.09.4**:

| Merkmal | Propanal `CCC=O` | Aceton `CC(=O)C` |
|---|---:|---:|
| Molmasse / g mol⁻¹ | 58,08 | 58,08 |
| TPSA / Å² | 17,07 | 17,07 |
| Wildman–Crippen logP, ungerundet | 0,5953 | 0,5953 |
| RDKit-rotierbare Bindungen | 1 | 0 |

**Folgerung:** Kein Beleg für einen Implementierungsfehler in diesen drei RDKit-Aufrufen. Identische berechnete logP-Werte sind eine **Modellgrenze**, kein Beleg gleicher experimenteller Verteilung; TPSA ist weder Dipolmoment noch tatsächliche geometrische Polaroberfläche. Die Rotationszählung ist kein vollständiges mechanisches Zählen aller physikalisch rotierbaren Einfachbindungen.

Zur experimentellen Größenordnung: Für Aceton wird **log Kₒw ≈ −0,24** angegeben (Environment and Climate Change Canada, experimentelle Daten); für Propanal enthalten Literatur/PubChem **Werte um +0,4 bis +0,6**. Messwert, Quellenart, Temperatur und Methode müssen bei Einbindung in die kuratierte Stoffdatenbank ausdrücklich dokumentiert werden. Auch experimentell können unterschiedliche Moleküle zufällig gleiche logP-Werte besitzen; Enantiomere haben in achiralen Phasen grundsätzlich gleiche Gleichgewichtswerte.

**Prüfpunkte für alle Moleküle:** gleichbleibende RDKit-Version für Regression, konsistente SMILES/Protonierungszustände, Sonderfälle bei ionischen und sehr großen Molekülen, TPSA-S-/P-Option bei geeigneten Verbindungen, Definitionsvarianten für Rotationszählung.

**Quellen:**
- RDKit Crippen: https://rdkit.org/docs/source/rdkit.Chem.Crippen.html
- RDKit TPSA: https://rdkit.org/docs/RDKit_Book.html
- RDKit Rotatable Bonds: https://rdkit.org/docs/source/rdkit.Chem.rdMolDescriptors.html
- Aceton log Kₒw: https://www.canada.ca/en/environment-climate-change/services/evaluating-existing-substances/screening-assessment13.html
- Propanal: https://pubchem.ncbi.nlm.nih.gov/compound/527

## 3. UX-Neuentwurf: Isomerenpaar als Ausgangspunkt

### A. Paar direkt auswählen

Sobald im Modul-Dropdown **Isomerie** eingestellt ist:
- statt eines einzelnen Moleküls steht das Dropdown **„Isomerenpaar“** im Vordergrund: 7 eindeutige kuratierte Paare;
- voreingestelltes Paar als übersichtliche Auswahl sichtbar;
- **„Vergleich anzeigen“** als primäre Aktion (die 2D-Vorschau kann ohne aufwendige Geometrieoptimierung sofort erscheinen);
- „Einzelmolekül untersuchen“ wird eine **optionale** Aktion oder Registerkarte, nicht die Voraussetzung für den Paarvergleich;
- bei anderen Modulen bleibt die bisherige Einzelmolekülsteuerung unverändert.

### B. Eine zusammenhängende Vergleichsfläche

```text
ISOMERIE    Vergleichspaar: [ Propanal ↔ Aceton  ▾ ]  [ Vergleichen ]

Leitfrage: Was bewirkt die andere Verknüpfung der Atome?

┌─────────────────────────────────────────────────────────┐
│ Propanal                       Aceton                    │
│ [2D-Struktur]                  [2D-Struktur]             │
│ Aldehyd                        Keton                     │
│ C₃H₆O                          C₃H₆O                     │
├─────────────────────────────────────────────────────────┤
│ GEMEINSAMER VERGLEICH – Merkmal | Propanal | Aceton      │
│  Struktur / Funktionelle Gruppen                        │
│  Summenformel               C₃H₆O      C₃H₆O            │
│  Carbonyl-C                  C+H        C+C              │
│  H-Brücken-Donoren              0          0             │
│  H-Brücken-Akzeptoren           1          1             │
│  Experimentelle Stoffeigenschaften                      │
│  Siedepunkt, °C               48–49      56,1           │
│  Wasserlöslichkeit            begrenzt   mischbar       │
│  log Kₒw (experimentell)     ≈ +0,4…0,6  ≈ −0,24         │
│  Reaktivität / Oxidation      Aldehyd     Keton          │
│  Modellwerte / Details [aufklappbar]                    │
│  TPSA, Å²                    17,07      17,07           │
│  logP (Wildman–Crippen)      0,60        0,60            │
│  Drehbare Bindungen (RDKit)     1           0            │
├─────────────────────────────────────────────────────────┤
│ [3D ansehen: Propanal | Aceton]   (eine 3D-Fläche)       │
│ [Einzelansicht optional] [MC-Frage] [Protokoll]          │
└─────────────────────────────────────────────────────────┘
```

Die Musterwerte sind **keine automatische neue Datengrundlage**: vor Freigabe Quellenprüfung und Zustand/Definition bestätigen. Gleiche Werte können dezent markiert werden; unterschiedliche, für die Leitfrage relevante Werte leicht hervorgehoben. Keine willkürlichen „richtig/falsch“-Farben an Stoffdaten.

Für fehlende Stoffwerte steht **„nicht hinterlegt“**, niemals `0` oder eine stillschweigend geschätzte Zahl.

### C. 3D ohne Breitenproblem

Standardmäßig zwei **2D-Strukturformeln nebeneinander**, was das Konnektivitätsproblem bei Isomeren unmittelbar verdeutlicht. Darunter auf Wunsch **ein gemeinsamer 3D-Viewer**, umschaltbar zwischen Isomer A und B; optionaler echter Side-by-Side-Modus erst auf breiten Bildschirmen nach Belastungstest. Ein einzelnes aus einer Optimierung erzeugtes 3D-Modell wird ausdrücklich als **Modellgeometrie** gekennzeichnet.

Die bisherige breite 3-Karten-Einzelanalyse (2D | 3D | Eigenschaften) bleibt als optionale Detailansicht verfügbar; sie soll die zentrale Gegenüberstellung nicht duplizieren.

## 4. Inhaltliche Kennzeichnung und Qualitätslogik

1. **Strukturbezogene, aus RDKit berechnete Angaben:** Formel, Molmasse, HBD/HBA, TPSA und Rotationsdeskriptor. Als Modell-/Definitionswerte kennzeichnen; TPSA und logP nicht mit einem Dipolmoment verwechseln.
2. **Kuratierte experimentelle Angaben:** Siedepunkt, Schmelzpunkt, Dichte, Wasserlöslichkeit, ggf. log Kₒw; mit Quellen und Bedingungen. Diese Werte bei Struktur–Eigenschaft-Fragen prominent darstellen.
3. **Qualitative chemische Einordnung:** erkannte Gruppen, Aldehyd/Keton, typische Reaktivität; keine quantitative Reaktionsprognose aus einer isolierten Struktur.
4. **Eigene Heuristik:** „Didaktischer Polaritätseindruck“ und „Wasserlöslichkeits-Tendenz“ aus `qualitative_polarity_assessment` **nicht als Stoffeigenschaft in der Haupttabelle anzeigen**; bis zur Validierung höchstens unter „vereinfachte Modellheuristik / experimentell nicht bestätigt“ oder aus der Isomerenansicht entfernen. Die aktuelle Einstufung „schwach/mäßig“ für beide Carbonylverbindungen ist irreführend.

Das ist nicht nur ein UI-Problem: Änderungen an den Deskriptoren und ihrer Interpretation wirken auch auf „Polarität und Löslichkeit“, „Konformere“, „Funktionelle Gruppen“ sowie „Wirkstoffe und Biomoleküle“. Deshalb werden Berechnungs-Regressionstests für alle 61 Moleküleinträge vorgeschlagen, die anderen Moduloberflächen aber vorerst **nicht** umgebaut.

## 5. Notebook-Einstieg ohne Entwicklerhistorie

- Erste Markdown-Zelle auf Titel, kurzen Lernzweck, vier Arbeitsschritte und „Laufzeit → Alle ausführen“ begrenzen.
- Entwicklungslog und Versionskommentare aus Anfang und Ende in `CHANGELOG.md` des Repositories verschieben (nicht löschen).
- Untere Zelle „Hinweise für weitere Versionen“ aus der Schüleransicht entfernen; stattdessen ggf. ein einziger kurzer Abschnitt „Interpretation und Modellgrenzen“ unmittelbar bei den Ergebnissen.
- Interne Versionsnummer bleibt klein sichtbar, die technischen Installations-/Funktionszellen bleiben funktionell erhalten.

## 6. Kleine Arbeitspakete und Definition der Abnahme

**Phase 1 – Fach-/Datenprüfung:** RDKit-Regressionswerte aller 61 Karten, Stoffdaten aus zwei dokumentierten Quellen pro heiklem Paar, Heuristikprüfung. Insbesondere das Testpaar Propanal/Aceton: gleiche Wildman–Crippen-Werte, aber unterschiedliche experimentelle log Kₒw-Werte; Aceton ist vollständig wasser-mischbar.

**Phase 2 – Layout ausschließlich für Isomerie:** eigene Paarwahl, gemeinsamer 2D-Vergleich, eine nach Datenart gegliederte Tabelle ohne Pandas-Index; 3D umschaltbar als optionales Detail; unveränderte MC-Prüfung und Protokollfunktion.

**Phase 3 – Regression über alle sieben Isomeriepaare:** einschl. Enantiomerie und geometrischer Isomerie; Stereomarker erhalten. Kein Stoffdatenwert wird erfunden oder automatisch aus anderer Substanz übernommen. Bestehende Polaritäts- und Konformerfunktionen bleiben benutzbar.

**Phase 4 – Werkstatt-Handbuch und MW-001/MW-009 anpassen:** Notebook-Anleitung auf **„Isomerie → Isomerenpaar auswählen → Vergleich anzeigen“** umstellen; Änderungen erst dann veröffentlichen, wenn die neue DIDACTIC-Oberfläche tatsächlich so funktioniert.

**Testfragen:** Liefert die Hauptansicht unmittelbar die zwei 2D-Strukturen, alle relevanten experimentellen Daten und deren Quellen? Lassen sich dieselben physikalisch unwidersprüchlichen Modellwerte korrekt einordnen? Ist die gesamte Ansicht mobil benutzbar? Funktionieren Antwortprüfung, 3D und Report weiterhin?

**Vorerst keine Änderung am Notebook, der Werkstatt oder an MOLLAB_PRO.** Dieses Dokument dient der fachlichen Abstimmung.
