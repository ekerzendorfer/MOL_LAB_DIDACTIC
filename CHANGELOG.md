# MOL_LAB DIDACTIC – Versions- und Entwicklungshinweise

Diese Datei enthält die technischen Versionsinformationen, die bis V0.4.2 am Anfang
und Ende des Colab-Notebooks angezeigt wurden. Die historischen Texte wurden
aus der Schüleroberfläche herausgenommen, nicht gelöscht.

## Ursprüngliche Titelseite (unverändert übernommen)

# MOL_LAB DIDACTIC v0.4.2

**Molekülwerkstatt für den Chemieunterricht der SEK2 – mit kuratierten Vergleichspaaren**

Ziel: Von der Molekülstruktur zu Stoffeigenschaften schließen.

Didaktischer Ablauf: **Beobachten → Vermuten → Antwort prüfen → Erklärung anzeigen**.

Diese Version nutzt bewusst nur schnelle, robuste Open-Source-Bausteine: RDKit, py3Dmol, ipywidgets und pandas. xTB/CREST bleiben im großen MOL_LAB.

> **v0.2:** kompakteres Layout mit Eigenschaften rechts neben 2D/3D, kompaktere Isomeren-Vergleichskarten und zusätzliche Sicherheit zum Neuaufbau der 3D-Anzeige.


> **v0.2:** alternative schlanke 3Dmol.js-Engine ergänzt, um Colab-Rendering-Probleme nach vielen 3D-Aufrufen abzufedern.


> **v0.4.2:** Modul *Polarität und Löslichkeit* enthält nun kuratierte Vergleichspaare mit Mini-Aufgaben und optionalem experimentellem Bezug. Die 3D-Darstellung wurde auf vier direkte Schaltflächen umgestellt.

## Ursprünglicher Schlussabschnitt (unverändert übernommen)

## 3. Hinweise für weitere Versionen

In v0.4.2 neu bzw. sichtbar aktiviert:
- einfacher SchülerInnen-Protokolltext über eine einzige Schaltfläche
- Reaktivitäts-Hinweise als aufklappbare Dreischritt-Erklärung: Hinweis – Warum? – Reaktionsidee
- Stoffdaten/experimenteller Bezug in Molekülvergleichen und Isomerenvergleichen
- JSON-Struktur bleibt Grundlage für spätere alternative Niveaustufen und einen möglichen Editor
- 3D-Rendering bleibt bewusst auf der stabilen v0.3.4-Logik


---

## Entwicklungszweig V0.5 – Isomerie und Deskriptoren

- Neues Forschungskonzept: Isomerenpaar im Vordergrund statt Einzelmolekül.
- RDKit-Deskriptorprüfung für alle 61 Einträge und sieben Isomeriepaare.
- Erklärte Trennung zwischen experimentellen Stoffdaten, RDKit-Modellwerten
  und nicht validierter didaktischer Polaritäts-/Löslichkeitsheuristik.
- Änderungen erfolgen auf `v0.5-isomerien-vergleich`; die Live-Version auf `main`
  bleibt während der Entwicklung unverändert.

## V0.5 – implementierter Entwurf, 24.11.2026

- Die Notebook-Titelseite wurde reduziert, die frühere untere Entwicklungsseite entfernt.
- Im Modul „Isomerie“ sind alle sieben Paare unmittelbar auswählbar.
- Neue kombinierte Vergleichsfläche mit 2D-Strukturen, Strukturmerkmalen, Stoffdaten, Reaktivität und getrennten erklärten RDKit-Deskriptoren.
- 3D-Viewer wird nur auf Anforderung aufgebaut und zwischen A/B umgeschaltet.
- Der Einzelmolekül-Workflow bleibt optional, die vier übrigen Module behalten die bisherigen Bedienelemente.
- Sieben eigens formulierte Isomerenpaar-MC-Fragen ergänzt.
- Umfangreiche Regression: 61 RDKit-Quellkarten, sieben Isomeriepaare, MC-Logik, Lazy-3D, Berichtstext und Modulumschaltung.
- Nach dem ersten Colab-Praxistest wurden vier quellenbelegte Isomerie-Stoffdatensätze ergänzt (Butan, Isobutan, Propansäure, Essigsäuremethylester), während offene Zucker-/Enantiomeren-Sonderfälle bewusst ohne erfundene Zahlen bleiben.
- Das ist **kein** Release auf `main`. Für die Freigabe fehlt die visuelle/chemiedidaktische Sichtung in Colab.

## V0.5-Nachbesserungen nach Nutzerprüfung, 24.11.2026

- Keine implizite Auswahl: Beim Öffnen von Isomerie muss zuerst ein Isomerenpaar ausgewählt und über „Vergleich anzeigen“ gestartet werden.
- Eigene, unabhängige 2D/3D/Oberflächen-Schaltflächen **direkt an jeder Molekülkarte**, statt eines einzigen späten Viewers unter der langen Tabelle.
- Qualitätsgrenze der farbigen 3D-Oberfläche: Jmol-Atomfarben auf VDW-Oberfläche, **keine** gemessene Polarität oder berechnetes elektrostatisches Potential.
- MC-Feedback und Erklärung erscheinen im jeweils sichtbaren Quiz direkt unter den Buttons, über einen live aktualisierten `widgets.HTML`-Wert.
- Tabellen unterdrücken leere Zeilen, bewahren die Modell-/Quelltrennung und ergänzen besondere Interpretationstexte bei D/L-Enantiomerie und offener Glucose/Fructose.
- WHO/ILO-ICSC und weitere Fachquellen für das Butan- und Säure/Ester-Paar; beide JSON- und Notebook-Fallback-Datensätze im Entwicklungszweig konsistent.
- GitHub-Actions-CI prüft alle sieben Paare, bewusste Auswahl, 2D/3D/qualitative Oberfläche, sämtliche MC-Buttons und alle vier weiteren Modulsteuerungen.

## V0.5 – Colab-Bedienkorrekturen, 24.11.2026

- Vier einzeln umbrechende MC-Auswahlzeilen statt fehlerhafter mehrzeiliger nativer RadioButtons; keine vorausgewählte Antwort.
- Einheitliche kompakte Strukturkarten und identische Anzeigebreite für 2D, 3D und Elementoberfläche.
- Unmittelbarer Start des Vergleichs nach Auswahl eines Paares; weiterhin kein automatischer Start beim bloßen Modulwechsel.
- UI-Regressionstests entsprechend aktualisiert; echte Colab-Abnahme steht aus.
