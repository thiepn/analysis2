# Methode der Themengewichtung

## Evidenzbasis

Die Auswertung verwendet 13 eigenständige Klausuren und 96 gebündelte Hauptaufgaben. Teilaufgaben werden nicht künstlich als eigenständige Aufgaben gezählt. Gleiche Aufgaben und klare Varianten werden zusätzlich über `duplicate_family` zusammengeführt. Dadurch stehen Rohhäufigkeit und Familienhäufigkeit nebeneinander.

## Formel

Der vorläufige Wert liegt zwischen 0 und 100 und ist die Summe dieser Komponenten:

| Komponente | Maximum | Berechnung |
|---|---:|---|
| Aktueller Kurs | 25 | `confirmed_current=25`, `likely_current=18.75`, `unresolved=8.75`, `historically_examined=7.5`, `likely_outdated=2.5` |
| Aktualität | 15 | linear vom ältesten Korpusjahr 2003 bis 2025 |
| Klausurbreite | 15 | Anzahl verschiedener Klausuren, bei 6 Klausuren gedeckelt |
| Einzigartige Aufgabenfamilien | 15 | relativ zum höchsten Familienwert eines Themas |
| Punktgewicht | 10 | anteiliges bekanntes Punktgewicht relativ zum höchsten Themenwert |
| Drei jüngste Klausuren | 10 | Anteil von SS 2025, Nachklausur SS 2021 und Klausur SS 2021 |
| Offizielle Lösungen | 5 | Anteil der Aufgaben mit offizieller Lösung oder offiziellem Schema |
| Quellenvertrauen | 5 | Mittel aus `hoch=1`, `mittel=0.7`, `niedrig=0.4` |

Aktuelle Übungsblätter erhalten nach einem späteren Upload eine eigene Komponente mit maximal 30 Punkten. Dann wird die Summe auf die jeweils verfügbaren Maximalpunkte normiert. Damit wiegt aktuelle Übungsevidenz stärker als jede einzelne historische Komponente. Solange keine Übungsblätter vorliegen, ist der Wert `not_provided`; er wird weder als null Evidenz interpretiert noch in die aktuelle 100-Punkte-Summe eingerechnet.

Die Prioritätsgruppe wird nicht nur aus dem Zahlenwert abgeleitet. `unresolved` bleibt immer **Ungeklärt**, historischer oder wahrscheinlich veralteter Stoff bleibt **C**. **A** verlangt bestätigte Skriptdeckung und entweder mindestens 60 Punkte oder mindestens einen Treffer in den drei jüngsten Klausuren bei mindestens 55 Punkten. Übriger skriptgedeckter Stoff ist **B**.

## Punktzuordnung

Wenn eine Hauptaufgabe mehrere Themen bündelt und keine Teilpunkte pro Thema nennt, werden ihre Punkte gleichmäßig auf die getaggten Themen verteilt. `known_point_task_exposure` enthält zusätzlich die ungeteilte Summe aller bekannten Punkte von Aufgaben, in denen das Thema vorkommt. Beide Werte sind analytische Schätzungen, keine offiziellen Themenpunktzahlen.

## Grenzen

- Nur sechs Klausuren haben vollständige oder rekonstruierbare Gesamtpunktzahlen; unbekannte Punkte werden nicht erfunden.
- SS 2025 ist die jüngste Evidenz, aber kein Beweis für den Prüfungsstoff 2026.
- Das aktuelle Skript bestätigt enthaltene Theorie, ersetzt jedoch keine offizielle Stoffabgrenzung.
- Differentialgleichungen, Mannigfaltigkeiten und mehrdimensionale Integration kommen 2025 vor, fehlen aber im Skript. Sie bleiben deshalb `unresolved` und werden nicht automatisch zu Priorität A.
- Das Thorbergsson-Dokument ist ein unvollständiges Erinnerungsprotokoll mit niedriger Quellenkonfidenz.
- Offizielle Lösungen erhöhen die Verlässlichkeit der Vorbereitung, nicht automatisch die fachliche Relevanz eines Themas.
