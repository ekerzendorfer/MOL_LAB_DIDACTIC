# MOL_LAB DIDACTIC – Daten- und Fragen-Audit

**Stand:** 23.11.2026 · **Aufgaben:** Qualitätsprüfung für die spätere systematische Ergänzung, keine Datenwerte erfinden.

## Prüfergebnis

- 61 Molekül-Einträge in fünf Modulen.
- Alle 61 Einträge besitzen vier Antwortoptionen und eine gültige Lösung – **das ursprüngliche Anzeigeproblem lag im Vergleichsmodus**.
- Sieben kuratierte Polaritäts-/Löslichkeitsvergleiche haben seit 23.11.2026 eigene Vergleichs-MC-Fragen; die sieben Isomerenpaare verwenden im Vergleichsmodus die bereits vorhandene Frage zum gewählten Ausgangsmolekül.
- Die ursprünglichen 61 Datensätze führen sämtlich die korrekte Antwort an Listenposition 0. Die Notebook-Oberfläche mischt die angezeigten Antworten seit dem aktuellen Fix, ohne die Datenstruktur zu verändern.
- **35 von 61 Molekül-Einträgen** haben noch keinen einzigen der fünf Stoffdaten-Werte (Schmelzpunkt, Siedepunkt, Dichte, Löslichkeit, Aggregatzustand) hinterlegt. Nicht jede Leerstelle ist durch Zahlenwerte sinnvoll schließbar: beispielsweise stehen *offenkettige Glucose/Fructose als Strukturmodelle* nicht für isolierte Reinstoffe dieser speziellen offenkettigen Konformation.
- Bei 7 Einträgen ist die MC-Frage als „Welche Aussage passt am besten?“ oder ohne konkrete Leitfrage formuliert; redaktionelle Präzisierung ist sinnvoll.

## Leere Stoffdatensätze nach Modul

| Modul | Moleküle | Ohne Stoffdaten |
|---|---:|---:|
| Polarität und Löslichkeit | 16 | 0 |
| Isomerie | 14 | 8 |
| Funktionelle Gruppen | 13 | 9 |
| Konformere | 7 | 7 |
| Wirkstoffe und Biomoleküle | 11 | 11 |

## Noch zu ergänzen oder bewusst als Modellfall kennzeichnen

- Isomerie: Butan
- Isomerie: Isobutan
- Isomerie: Propansäure
- Isomerie: Essigsäuremethylester
- Isomerie: D-Alanin
- Isomerie: L-Alanin
- Isomerie: Glucose offen
- Isomerie: Fructose offen
- Funktionelle Gruppen: Ethanal
- Funktionelle Gruppen: Ethylacetat
- Funktionelle Gruppen: Acetanhydrid
- Funktionelle Gruppen: Ethylamin
- Funktionelle Gruppen: Acetamid
- Funktionelle Gruppen: Phenol
- Funktionelle Gruppen: Anilin
- Funktionelle Gruppen: Salicylsäure
- Funktionelle Gruppen: Vanillin
- Konformere: Butan
- Konformere: 1,2-Dichlorethan
- Konformere: Ethylenglykol
- Konformere: Cyclohexan
- Konformere: Milchsäure
- Konformere: n-Pentan
- Konformere: 2-Butanol
- Wirkstoffe und Biomoleküle: Coffein
- Wirkstoffe und Biomoleküle: Aspirin
- Wirkstoffe und Biomoleküle: Paracetamol
- Wirkstoffe und Biomoleküle: Ibuprofen
- Wirkstoffe und Biomoleküle: Acetazolamid
- Wirkstoffe und Biomoleküle: Glycin
- Wirkstoffe und Biomoleküle: Alanin
- Wirkstoffe und Biomoleküle: Phenylalanin
- Wirkstoffe und Biomoleküle: Adenin
- Wirkstoffe und Biomoleküle: Ribose
- Wirkstoffe und Biomoleküle: Citronensäure

## Redaktionell schwache MC-Leitfragen

- Isomerie: L-Alanin – Welche Aussage passt am besten?
- Isomerie: Fructose offen – Welche Aussage passt am besten?
- Wirkstoffe und Biomoleküle: Paracetamol – Welche Aussage passt am besten?
- Wirkstoffe und Biomoleküle: Ibuprofen – Welche Aussage passt am besten?
- Wirkstoffe und Biomoleküle: Acetazolamid – Welche Aussage passt am besten?
- Wirkstoffe und Biomoleküle: Alanin – Welche Aussage passt am besten?
- Wirkstoffe und Biomoleküle: Phenylalanin – Welche Aussage passt am besten?

## Vorgehen für weitere Qualitätsrunde

1. **Isomeriepaare priorisieren**, weil die Vergleichsansichten jeweils zwei vollständige, konsistente Spalten brauchen (Butan/Isobutan, Propansäure/Methylacetat, stereochemische Paare).
2. Daten nur mit **Stoffform, Temperatur, Druck, Quelle** und Besonderheiten der Vergleichbarkeit ergänzen. Schmelzpunkt und Dichte sind bei Gasen, Zwitterionen, Lösungen oder rein konzeptionellen Strukturformen besonders zu prüfen.
3. Bei Stereoisomeren oder offenkettigen Zuckermodellen bewusst Grenzen benennen, statt Scheinpräzision zu erzeugen.
4. MC-Fragen fachlich auf *die Leitfrage des konkreten Vergleichs* ausrichten; Distraktoren prüfen, Positionen mischen, Erklärung nicht vorab verraten.
5. Für jede Änderung: JSON und eingebettete Colab-Fallback-Daten konsistent halten; Beispiel im Notebook einmal tatsächlich durchspielen.

## Bereits korrigiert

- Ethanol/Dimethylether: Dimethylether-Stoffdaten/Reaktivität einschließlich Flüssigkeitsdichte-Warnung.
- Propanal/Aceton: Propanal-Stoffdaten (NIST/PubChem/EPA) und Aldehyd-Reaktivität ergänzt.
- MC-Prüfung bei Isomeren- und Polaritätsvergleichen aktiviert; ergänzende kuratierte Vergleichsfragen für alle sieben Polaritätspaare.

**Status:** Weitere Ergänzungen aus dieser Liste sind noch offen. Das ist bewusst ein separater didaktischer Qualitätsschritt und kein verdeckter automatischer Datenimport.
