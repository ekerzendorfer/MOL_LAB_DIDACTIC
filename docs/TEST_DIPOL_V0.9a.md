# DIDACTIC V0.9a – Colab-Abnahme (Wasser)

1. [Entwicklungsnotebook öffnen](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/v0.9a-dipol-labor/MOL_LAB_DIDACTIC_v0_4_2.ipynb); frische Laufzeit → Alle ausführen. Kopfzeile V0.9a · Entwurf.
2. Polarität und Löslichkeit → Einzelmolekül Wasser → Molekül analysieren. Unter dem normalen Struktur-/Eigenschaftenbereich Button „Bindungsdipole untersuchen“. Kein automatisches zusätzliches 3D-Fenster.
3. Button öffnen. 1 · Geometrie: Wasser frei drehen; zunächst keine EN-Werte/Pfeile.
4. 2 · EN-Werte: H 2,20 (zweimal), O 3,44. Labels lesbar und am jeweiligen Atom verankert; aus mehreren Blickrichtungen prüfen.
5. 3 · Bindungsdipole: zwei blaue gleich lange Pfeile H → O, parallel zu den Bindungen, mit Querstrich an der H-Seite; ΔEN 1,24. Prüfen, ob Pfeile und Labels genügend Platz haben.
6. Beim Wechsel zwischen Stufen muss die Orientierung erhalten bleiben. Zurück zu Geometrie: keine Pfeile/Labels mehr. Mehrfach wiederholen. Schließen und neu öffnen darf die Ansicht neu initialisieren.
7. Anderes Einzelmolekül, Paarvergleich, MW-024: keine neue Dipol-Funktion, bisherige Ansicht weiterhin intakt.

Grenzen: qualitative EN-Pfeile, keine Debye-Werte, chemische Pfeilrichtung entgegengesetzt zum physikalischen Dipolmomentvektor. Nur Wasser ist aktiviert. Keine Vektorsumme oder allgemeine Dipolmomentberechnung in V0.9a. V0.9b folgt erst nach Sichtprüfung. Automatisierte Tests prüfen Geometrie und JS-Interaktionen mit Mock, nicht tatsächliches WebGL-Rendering in Colab.
