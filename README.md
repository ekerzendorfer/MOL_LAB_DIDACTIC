# MOL_LAB DIDACTIC v0.4.2

**Molekülwerkstatt für den Chemieunterricht der SEK2**  
Didaktisch reduzierte Colab-App zur Untersuchung von Struktur, räumlicher Gestalt, Polarität, Löslichkeit, Isomerie, funktionellen Gruppen, Konformeren und einfachen Struktur–Eigenschafts-Beziehungen.

[![In Colab öffnen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_4_2.ipynb)

## Neu in v0.4.2

- **SchülerInnen-Protokolltext** über eine einzige Schaltfläche
- **Reaktivitäts-Hinweise** als aufklappbare Dreischritt-Erklärung: *Hinweis – Warum? – Reaktionsidee*
- **Stoffdaten / experimenteller Bezug** in kuratierten Molekülvergleichen und Isomerenvergleichen
- JSON-Struktur weiter stabilisiert; alternative Niveaustufen und ein späterer Editor bleiben vorbereitet
- 3D-Rendering bleibt bewusst unverändert gegenüber v0.3.4, um die Stabilität zu erhalten

## Dateien

```text
MOL_LAB_DIDACTIC_v0_4_2.ipynb
molecules_v0_4_2.json
README.md
```

Alle Dateien sollten im Root-Verzeichnis des Repos liegen.

## Start in Google Colab

```text
https://colab.research.google.com/github/ekerzendorfer/MOL_LAB_DIDACTIC/blob/main/MOL_LAB_DIDACTIC_v0_4_2.ipynb
```

In Colab anschließend: **Laufzeit → Alle ausführen**.

## Didaktisches Prinzip

MOL_LAB DIDACTIC ist kein Molekülkatalog und keine wissenschaftliche Datenbank. Die Beispiele sind kuratiert und sollen typische Fehlvorstellungen aufbrechen, etwa:

- gleiche Summenformel bedeutet nicht gleiche Stoffeigenschaft,
- polare Bindungen bedeuten nicht automatisch polares Molekül,
- eine polare funktionelle Gruppe garantiert keine gute Wasserlöslichkeit,
- kleine Strukturunterschiede können physikalische Eigenschaften und Reaktivität stark verändern.

## Grenzen

Die angezeigten Werte sind Modellwerte oder kuratierte Unterrichtsdaten. Reaktivitäts-Hinweise sind qualitative Orientierung anhand funktioneller Gruppen und ersetzen keine vollständige Reaktionslehre.


## Änderungen in v0.4.2

- Multiple-Choice-Fragen markieren nicht mehr automatisch die erste Antwort.
- Antwortprüfung ist gegen Vergleichsberichte abgesichert.
- Kleine Start-/UI-Korrekturen für die Antwortprüfung.


## Änderungen in v0.4.2

- Feinschliff der Multiple-Choice-Fragen: plausiblere Distraktoren statt offensichtlich falscher Antworten.
- Reaktivitäts-Hinweise textlich vereinheitlicht: Hinweis – Warum? – Reaktionsidee.
- Konformer-Modul um **n-Pentan** und **2-Butanol** ergänzt.
- JSON-Metadaten für spätere einklappbare Bereiche vorbereitet, ohne die Oberfläche zu verändern.
- Plus-Beispiele bleiben bewusst noch zurückgestellt.


## Datenkorrektur 23.11.2026 – Isomerie-Vergleich Ethanol/Dimethylether

Die bislang leeren Stoffdaten- und Reaktivitätsfelder für Dimethylether sind ergänzt. Die Dichte ist ausdrücklich als **Flüssigkeitsdichte unter Druck** gekennzeichnet. Datenquellen: PubChem CID 8254, NIST Chemistry WebBook, FSANZ A1062.

Nach einem GitHub-Update in einer bereits laufenden Colab-Sitzung die Zelle **„MOL_LAB DIDACTIC starten“ erneut ausführen**, um die aktuelle JSON einzulesen; sofern nötig „Laufzeit → Neu starten“ und die Zellen erneut ausführen. Die Vergleichsroutine wurde nicht verändert.

## Qualitätsprüfung der Vergleichsaufgaben (November 2026)

Die Daten und Antwortprüfung wurden für die MOLEKÜL-WERKSTATT überarbeitet: Propanal-Stoffdaten/Reaktivität ergänzt, Multiple-Choice bei den Isomeren- und Polaritätsvergleichen aktiviert und die Antwortreihenfolge variiert. Weitere `35` von `61` Molekül-Einträgen haben noch keine Stoffdaten; manche (z. B. „Glucose offen“) sind bewusst Strukturmodelle und dürfen nicht mit Reinstoffdaten verwechselt werden.

Die vollständige Aufstellung und Reihenfolge für die spätere fachliche Feinarbeit steht unter [Datenqualität-Audit](docs/DATENQUALITAET_AUDIT_2026-11-23.md).
