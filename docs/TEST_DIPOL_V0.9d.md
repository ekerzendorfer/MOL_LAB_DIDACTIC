# DIDACTIC V0.9d – Experimenteller Bezug

Abgenommene V0.9c ist die Basis. Keine Änderungen der Geometrie, Vektoren oder Konstruktion. Neu: nach dem letzten Schritt der Vektoraddition erscheint ein zunächst geschlossenes Details-Feld, das beim Zurückschalten geschlossen und verborgen wird.

| Molekül | Gasphasen-Referenz | Grundlage |
|---|---:|---|
| CO₂ | 0 D | Symmetrie D∞h, NSRDS-NBS10 |
| H₂O | 1,85498 D (Anzeige ≈ 1,855 D) | μ₀, Shostak/Ebenstein/Muenter 1991, DOI 10.1063/1.460471 |
| NH₃ | 1,476 D | μ₀, Shimizu 1970, DOI 10.1063/1.1673524 |
| CH₄ | 0 D | Symmetrie Td, NSRDS-NBS10 |

Quelle: [NIST CCCBDB – experimental dipole moments](https://cccbdb.nist.gov/diplistx.asp), geprüft 28.11.2026. H₂O: μ₀ statt Gleichgewichtswert μe = 1,857 D. NH₃: Datenbank-Hauptwert 1,476 D. Nullwerte sind Symmetrie-Referenzen, nicht Messwerte mit drei signifikanten Nachkommastellen.

## Praktische Abnahme
- [ ] Bei allen vier Beispielen erscheint die Referenz erst im letzten Additionsschritt; zunächst geschlossen.
- [ ] Alle vier Werte, Einheit und Modellgrenzen korrekt; Quellenlink funktioniert.
- [ ] Beim Zurückschalten verschwinden Referenzen; Orientierung und Vektoren bleiben wie V0.9c.
- [ ] MW-015 führt zu allen vier Beispielen und dem optionalen experimentellen Bezug; Notizen bleiben je Molekül getrennt.

Noch keine Freigabe auf main. Die allgemeine Dipolmomentberechnung und weitere Sets sind bewusst nicht enthalten.

## Gesamtfreigabeprüfung MW-015 – 28.11.2026

- [x] Experimenteller Bezug erst nach dem letzten Additionsschritt.
- [x] Referenzwert, Quellenangabe und Modellgrenze verständlich.
- [x] Zurückschalten verbirgt Referenz.
- [x] Werkstatt-Anleitung verständlich.
- [x] Vollständiger Forschungsweg mit Protokoll funktioniert.

5/5 praktische Prüfpunkte bestanden. Abgenommene V0.9d-Programmquelle: `41229838aad18bfc7d973fdfef297ee20a149b04`, [Regression erfolgreich](https://github.com/ekerzendorfer/MOL_LAB_DIDACTIC/actions/runs/46147361353). Zwei spätere Colab-Speicherstände enthielten nach Vergleich exakt die V0.9c-Programmquelle (ohne experimentellen Bezug) und Ausgaben; jüngster Stand `d25e27264f2ecb21c2c2a1bb6249828205039086` mit fehlgeschlagener Regression. Die abgenommene V0.9d-Notebookdatei wird byteidentisch durch einen neuen Commit wiederhergestellt; die Colab-Speicherstände bleiben in der Historie erhalten. Kein Force-Push. Freigabe auf main erst nach erneut erfolgreicher Regression.

## Freigabe – 28.11.2026

Anwender bestätigt abschließend alle Kontrollen und autorisiert Veröffentlichung auf main. Wiederhergestellte V0.9d: [Regression erfolgreich](https://github.com/ekerzendorfer/MOL_LAB_DIDACTIC/actions/runs/46149331775). Für V0.9 werden nur Versionsanzeige, Einleitung und Freigabedokumentation geändert; Modellcode bleibt unverändert. Stabile Colab-Adresse wie bisher über main.
