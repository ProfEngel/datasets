# Relmiad ONE · Sneaker-Datenwerkstatt

Vollständig **fiktive, reproduzierbar generierte Lehrdaten**, Stand 16.11.2026,
Version 1.0.0. Keine echten Kunden, Messungen oder Geschäftsergebnisse.

| Datei | Verwendung |
|---|---|
| produkt.csv | Ein fiktiver Limited-Edition-Sneaker, SKU und Nettolistenpreis |
| bi_bestellungen_historisch.csv | 300 Bestellungen; BI zu Absatz, Erlös und Retouren |
| bestellungen_train_roh.csv | 102 Zeilen mit Dubletten, fehlendem Wert und Prozentstring |
| bestellungen_train_sauber.csv | 100 ursprüngliche Generatorfälle, nur eine Lehrreferenz |
| bestellungen_validierung.csv | 40 neue Fälle zur Entwicklungs-/Modellwahl |
| bestellungen_test.csv | 40 reservierte Fälle; erst nach eingefrorener Auswahl prüfen |
| bestellungen_neu.csv | 12 unbekannte Fälle ohne Retourenziel |
| absatz_wochen.csv | 12 konstruierte Wochenwerte für Regression |
| absatz_zukunft.csv | Vier zukünftige Szenarien OHNE Ist-Absatz |
| rezensionen.csv | Zwölf erfundene Rezensionen für Textauswertung |

Bitte zuerst [DATENPASS.md](DATENPASS.md) lesen. [datenmanifest.json](datenmanifest.json)
enthält Schema, Zeilenzahlen und SHA-256. UTF-8, Komma als Separator,
Dezimalpunkt, ISO-Datum. Rohdaten nicht überschreiben. IDs sind keine Features.

**Drei getrennte Einheiten:** ein Schuh im Statistik-Einstieg; eine Bestellung
für Klassifikation/BI; eine Woche für Absatzregression. BI- und ML-Bestellungen
sind verschiedene Bestände. Keine Join- oder Modellgütebehauptungen erfinden.
Fehlende Zielwerte der Zukunft erlauben Vorhersagen, aber keine Gütemessung.
Kleine synthetische Tests sind keine Produktionsfreigabe.

Herkunft: eigener Lehrfall von Prof. Dr. Mathias Engel, mit generativer
KI-Unterstützung und deterministischem Generator. Generator und Datenpass
liegen bei. Es gilt die LICENSE im Repository-Stamm; diese Ergänzung ändert
keine Rechte oder Lizenzen anderer Datensätze des Repositories.
