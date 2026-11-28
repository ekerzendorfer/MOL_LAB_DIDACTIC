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
