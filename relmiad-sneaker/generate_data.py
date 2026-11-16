"""Reproducible fictional teaching fixtures. No personal data, no API calls."""
import csv,json,random,math,hashlib,datetime
from pathlib import Path

def make_orders(seed,n,prefix):
    r=random.Random(seed);rows=[]
    for i in range(n):
        fit=round(r.uniform(0,2),2);discount=r.choice([0,5,10,15,20,25,30])
        probability=1/(1+math.exp(-(-3+2.8*fit+.035*discount)))
        rows.append(dict(ID=f'{prefix}{i+1:03d}',Passformabweichung_cm=fit,Rabatt_Prozent=discount,Retoure=int(r.random()<probability)))
    return rows

def build(base,folder=None,emit_js=True):
    folder=folder or base/'material/sneaker-labor';folder.mkdir(parents=True,exist_ok=True)
    train=make_orders(701,100,'T');valid=make_orders(702,40,'V');test=make_orders(703,40,'P')
    future=[{k:v for k,v in row.items() if k!='Retoure'} for row in make_orders(704,12,'N')]
    raw=[dict(row) for row in train];raw[2]['Passformabweichung_cm']='';raw[6]['Rabatt_Prozent']='10 %';raw.extend([dict(raw[0]),dict(raw[1])])
    sales=[dict(Woche=i,Werbebudget_100EUR=i,Absatz_Paare=round(25+6*i+random.Random(800+i).uniform(-8,8))) for i in range(1,13)]
    reviews=['Die Sohle ist bequem und der Schuh passt.','Die Größe ist zu klein. Retoure wegen Größe.','Bequem und leicht. Die Sohle gefällt.','Die Lieferung war schnell.','Die Größe passt, der Schuh ist bequem.','Die Sohle ist hart.','Lieferung spät, aber bequem.','Die Farbe gefällt.','Größe zu groß, Retoure.','Der Preis ist hoch.','Sohle und Farbe sind gut.','Bequem, leicht und gute Verarbeitung.']
    r=random.Random(1701);bi=[]
    for i in range(300):
        qty=r.choice([1,1,1,1,2]);price=129.;discount=r.choice([0,0,5,10,15,20]);returned=int(r.random()<.16);revenue=round(qty*price*(1-discount/100),2)
        bi.append(dict(Bestell_ID=f'BI{i+1:04d}',Datum=(datetime.date(2026,1,1)+datetime.timedelta(days=i)).isoformat(),SKU='RO-LE-01',Kanal=r.choice(['Webshop','Filiale']),Region=r.choice(['Nord','Sued','Ost','West']),Groesse_EU=r.choice([38,39,40,41,42,43,44,45,46]),Menge_Paare=qty,Listenpreis_netto_EUR=price,Rabatt_Prozent=discount,Retoure=returned,Umsatz_netto_vor_Retoure_EUR=revenue,Umsatz_netto_nach_Retoure_EUR=0 if returned else revenue))
    future_sales=[dict(Woche=i,Werbebudget_100EUR=v) for i,v in [(13,7),(14,9),(15,11),(16,15)]]
    files=[('bestellungen_train_roh.csv',raw),('bestellungen_train_sauber.csv',train),('bestellungen_validierung.csv',valid),('bestellungen_test.csv',test),('bestellungen_neu.csv',future),('absatz_wochen.csv',sales),('absatz_zukunft.csv',future_sales),('rezensionen.csv',[dict(ID=i+1,Text=t) for i,t in enumerate(reviews)]),('bi_bestellungen_historisch.csv',bi),('produkt.csv',[dict(SKU='RO-LE-01',Produkt='Relmiad ONE',Edition='Limited Edition',Farbe='weiss',Listenpreis_netto_EUR=129)])]
    for name,rows in files:
        with (folder/name).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    data=dict(train=train,valid=valid,test=test,future=future,sales=sales,reviews=reviews)
    if emit_js:(base/'assets/js/sneaker-data.js').write_text('window.SneakerData='+json.dumps(data,ensure_ascii=False)+';')
    (folder/'DATENPASS.md').write_text('''# Relmiad ONE – fiktive Lehrdaten

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
''')
    index=[]
    for name,rows in files:index.append(dict(file=name,rows=len(rows),columns=list(rows[0]),sha256=hashlib.sha256((folder/name).read_bytes()).hexdigest(),url='https://raw.githubusercontent.com/ProfEngel/datasets/main/relmiad-sneaker/'+name))
    manifest=dict(version='1.0.0',created='2026-11-16',fictional=True,personalData=False,repository='https://github.com/ProfEngel/datasets/tree/main/relmiad-sneaker',files=index,license='See repository root LICENSE; no independent license change.')
    (folder/'datenmanifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    (folder/'README.md').write_text('''# Relmiad ONE · Sneaker-Datenwerkstatt

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
''')
    return data

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description='Generate entirely fictional Relmiad teaching data, no APIs.');p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent)
    args=p.parse_args();build(Path(__file__).resolve().parent,folder=args.out,emit_js=False)
