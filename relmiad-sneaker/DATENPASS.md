# Relmiad ONE – fiktive Lehrdaten

Keine echten Kunden, Messungen oder Verkäufe. Kein empirischer Leistungsnachweis.
Bestellungen: eine Zeile je Bestellung für ein Paar desselben Sneakers.
Prognosezeitpunkt: Bestellung. Passformabweichung: absoluter Abstand einer
angegebenen Fußlänge zur empfohlenen Passform in cm; Rabatt in Prozent. Diese
Angaben gelten im Lehrfall als vor der Retoure verfügbar. Retoure ist das später
bekannte Ziel (0 behalten, 1 retourniert). ID ist nur ein Schlüssel, kein Merkmal.
Ein einzelner Schuh bleibt dagegen die Einheit der Statistik-Einstiegsfolien.

100 Trainingsbestellungen, 40 Validierungsfälle, 40 reservierte Testfälle;
12 neue Fälle ohne Ziel. Rohdatei enthält zwei doppelte IDs, einen fehlenden
Passformwert und einen Prozentstring. Saubere Referenzdatei enthält die
ursprünglichen Generatorwerte: NICHT so tun, als könne man einen fehlenden
echten Wert rekonstruieren. Im eigenen Modell fehlende Werte begründet und
nur aus Trainingsdaten behandeln. Aufteilung vor dem Fitten der Vorverarbeitung.
Neufälle dürfen vorhergesagt, aber ohne spätere Zielwerte nicht bewertet werden.

Die HTML-Simulation trainiert eine kleine logistische Regression und einen
Entscheidungsstumpf auf dem sauberen Trainingssplit. Validierung dient Auswahl;
Test ist bis zur ausdrücklichen Abschlussöffnung verborgen. Kein Cross-Validation-
oder Produktivnachweis. Clustering verwendet nur Merkmale, keine Retourenlabels.
Absatz: eine Zeile je fiktive Woche, Werbebudget in 100 EUR, Absatz in Paaren.
Beobachteter Zusammenhang ist keine kausale Werbewirkung. Rezensionen erfunden.

BI-Bestellungen sind ein separater synthetischer Bestand mit BI-Präfix; NICHT
mit den Trainingsbestellungen T/V/P/N gleichsetzen oder per Zeilennummer joinen.
Eine Zeile ist eine Bestellung, Menge in Paaren. Ausschließlich vollständige
Retouren angenommen. Nettoerlös nach Retoure: zurückgegebene Bestellung = 0,
sonst rabattierter Nettoerlös. Keine Steuern, Versand-, Einkaufs- oder
Marketingkosten berücksichtigt; deshalb NICHT Gewinn nennen. Retourenquote
nach Bestellungen und nach Paaren getrennt benennen. Produkt-SKU als geprüfter
Many-to-one-Join mit produkt.csv. Zukunftsabsatz hat absichtlich keinen Ist-Absatz;
Woche 16 mit Budget 15 liegt außerhalb des historischen Budgetbereichs 1–12.
Offen als Extrapolation markieren. Alle Zukunftsfälle bleiben ungeprüft, bis
echte (hier nur später ergänzbare Lehr-)Zielwerte vorliegen.
