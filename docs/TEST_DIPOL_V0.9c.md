# DIDACTIC V0.9c – Abnahme NH₃ und CH₄

[Colab öffnen](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/v0.9c-basisset/MOL_LAB_DIDACTIC_v0_4_2.ipynb), Laufzeit → Alle ausführen. Polarität und Löslichkeit → Ammoniak bzw. Methan → Molekül analysieren → Bindungsdipole untersuchen.

- [ ] NH₃: trigonal-pyramidal, EN H 2,20 / N 3,04, drei H → N Pfeile, ΔEN 0,84.
- [ ] NH₃: fünf Konstruktionsschritte, offene Kette, grüne Summe entlang der dreizähligen Achse Richtung N; letzter Pfeil seitlich versetzt.
- [ ] CH₄: tetraedrisch, EN H 2,20 / C 2,55, vier H → C Modellpfeile, ΔEN 0,35.
- [ ] CH₄: sechs Konstruktionsschritte, vier verschiedenfarbige Vektoren schließen räumliches Polygon exakt; Nullsumme ohne grünen Richtungspfeil.
- [ ] Vor-/Zurück und Stufenwechsel ohne Rücksetzen der Orientierung, Lesbarkeit und Zoom bei beiden.
- [ ] H₂O und CO₂: bisheriger Ablauf unverändert, insbesondere seitlich verschobene H₂O-Resultierende.
- [ ] Andere Module unverändert.

Nur im Dipol-Lernmodus: NH₃ dreizählig symmetrisiert mit mittlerer axialer Projektion der RDKit-Geometrie, CH₄ ideal tetraedrisch mit mittlerer Bindungslänge. Originalkoordinaten der regulären Analyse unverändert. Gleich lange qualitative Bindungsvektoren innerhalb eines Moleküls, chemische Pfeilkonvention; keine quantitative Dipolberechnung. Freie Elektronenpaare wirken auf die reale Elektronendichte; das vereinfachte Bindungsmodell ist keine vollständige physikalische Zerlegung. Experimentelle Referenzwerte folgen gesondert nach visueller Abnahme. Automatische Tests prüfen Mathematik und JS-Mock, nicht die tatsächliche WebGL-Darstellung.

## Praktische Abnahme – 28.11.2026

- [x] NH₃: Molekülgestalt und EN-Beschriftungen korrekt.
- [x] NH₃: Alle drei Bindungsdipolpfeile sichtbar und richtig gerichtet.
- [x] NH₃: Vektoraddition mit fünf Schritten nachvollziehbar.
- [x] NH₃: Grüne Resultierende korrekt neben dem Molekül.
- [x] CH₄: Molekülgestalt und EN-Beschriftungen korrekt.
- [x] CH₄: Alle vier Bindungsdipolpfeile sichtbar und richtig gerichtet.
- [x] CH₄: Räumliches Vektorpolygon schließt sich nachvollziehbar.
- [x] CH₄: Nullsumme korrekt dargestellt.
- [x] Vor-/Zurückschalten und räumliche Rotation funktionieren.
- [x] H₂O und CO₂ funktionieren weiterhin wie in V0.9b.1.

Alle zehn praktischen Prüfpunkte bestanden. Abgenommener Programmcommit: `cb37f0b52982430284ab2da669314c3289f0e76d`. [Vollständige automatisierte Regression](https://github.com/ekerzendorfer/MOL_LAB_DIDACTIC/actions/runs/46146118778): erfolgreich. Symmetriegruppen: CO₂ D∞h, H₂O C₂v, NH₃ C₃v, CH₄ Td. Die separate Prüfung der übrigen Module erfolgte durch automatisierte Regression; das vorliegende Nutzerprotokoll betrifft die zehn aufgeführten Punkte. Nächste Schritte: experimentelle Referenzwerte separat kennzeichnen und MW-015 integrieren; keine Veröffentlichung auf main vor Gesamtfreigabe.
