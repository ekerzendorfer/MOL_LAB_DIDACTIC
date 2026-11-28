# DIDACTIC V0.9b – praktische Abnahme
 
[Notebook in Colab öffnen](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/v0.9b-vektoraddition/MOL_LAB_DIDACTIC_v0_4_2.ipynb). Laufzeit → Alle ausführen; Polarität und Löslichkeit → Wasser bzw. Kohlenstoffdioxid → Molekül analysieren → Bindungsdipole untersuchen.

- [ ] Wasser: Stufen 1–3 wie in V0.9a.
- [ ] CO₂: lineare Form, C 2,55, O 3,44, zwei Pfeile C → O; ΔEN 0,89.
- [ ] Stufe 4: erster freier Vektor, zweiter an dessen Spitze, Resultierende, Übertragung an das Molekül.
- [ ] Wasser: grüner Vektor in Richtung O auf der Winkelhalbierenden; Länge bleibt beim Verschieben gleich.
- [ ] CO₂: entgegengesetzte Pfeile (blau breiter, orange schmaler auf demselben Weg), Rückkehr zum Ausgangspunkt, Nullsumme; kein grüner Richtungspfeil.
- [ ] Vor-/Zurück, Wechsel Stufe 3/4 und freies Drehen ohne Rücksetzen der Orientierung.
- [ ] Lesbarkeit, Platz und Pfeilgrößen bei beiden Molekülen.
- [ ] Sonstige DIDACTIC-Funktionen unverändert.

Nur qualitative gleich lange Modellvektoren, keine Debye. Chemische Pfeilkonvention. CO₂-Geometrie im Lernmodus idealisiert; normaler Viewer unverändert. Die JS-Tests verwenden einen Mock, keine visuelle WebGL-Abnahme. NH₃/CH₄ und experimentelle Referenzwerte folgen V0.9c.

## Praktische Abnahme – 28.11.2026 (V0.9b)

- [x] H₂O: bisherige drei Stufen unverändert.
- [x] CO₂: EN-Werte und Bindungsdipole korrekt.
- [x] H₂O: schrittweise Vektoraddition verständlich.
- [ ] H₂O: grüne Resultierende – Richtung laut Anwender korrekt, Spitze aber vom O-Atom verdeckt. Sichtkontrolle nach Korrektur offen.
- [x] CO₂: vollständige Kompensation nachvollziehbar.
- [x] Vorwärts und rückwärts schalten funktioniert.
- [x] Räumliche Orientierung bleibt erhalten.
- [x] Größenverhältnisse, Farben und Lesbarkeit zufriedenstellend.

7/8 Prüfpunkte bestanden. [Regression des geprüften Stands](https://github.com/ekerzendorfer/MOL_LAB_DIDACTIC/actions/runs/46144224024) erfolgreich.

### V0.9b.1 – Darstellungskorrektur

Nur die Position der abschließenden grünen Resultierenden bei nicht verschwindender Summe wird geändert: seitlich neben das Molekül verschoben, mit mindestens 0,60 Å Abstand der Pfeilachse zu allen Atomzentren. Betrag und Richtung bleiben identisch zur konstruierten Summe. Die Hilfsfunktion ist für die spätere NH₃-Erweiterung wiederverwendbar. Bei CO₂ bleibt die Nullsumme unverändert; bei CH₄ ist später ebenfalls kein Richtungspfeil vorgesehen. Keine Garantie gegen projektionsbedingte Überdeckung aus jeder Blickrichtung; durch Drehen ist die räumliche Trennung sichtbar. Noch offen: Colab-Sichtprüfung der letzten Stufe bei Wasser.
