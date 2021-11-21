import csv
from os import linesep
with open("vstup.csv", encoding="utf-8") as csvinfile,\
	 open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile:
	# Vytvoříme proměnnou `reader` držící objekt pro čtení z `csvinfile`
	reader = csv.reader(csvinfile, delimiter = ",")
	# Vytvoříme proměnnou `writer`, jak pro tydenni prumery tak pro rocni držící objekt pro zápis do `csvoutfile`
	writertyden = csv.writer(csvoutfile)
	writerrok = csv.writer(csvoutfile)
	# Vytvorime si proměnné sedmiprum(prumer za 7 dni) a promennou cisloradky
	sedmiprum = 0
	cisloradky= 0
	zbytek = 0	
	# Cyklus, který projede všechny řádky v souboru
	for row in reader:		# Čteme jednotlivé řádky z `reader`u, v `row` máme seznam buněk daného řádku
		# Zjišťujeme zda je cisloradky delitelné 7
		if cisloradky % 7 == 0:
			prvnidensedmice = row
		# Přiřadí do sedmiprum, denni prumer z aktualni radky
		try:
				sedmiprum = sedmiprum + float(row[5])
				zbytek = zbytek + 1		
		except ValueError:
			print("Na řádku je chybná hodnota")

		if cisloradky % 7 == 6:
			sedmiprum=sedmiprum/7
			sedmiprum ="{:.4f}".format(sedmiprum)
			prvnidensedmice[5]= sedmiprum
			writertyden.writerow(prvnidensedmice)
			zbytek= zbytek - 1
			sedmiprum= float(sedmiprum)
			sedmiprum=0
		cisloradky= cisloradky + 1
	if cisloradky % 7 != 6:
		sedmiprum = sedmiprum / zbytek
		sedmiprum = "{:.4f}".format(sedmiprum)
		prvnidensedmice[5] = sedmiprum
		writertyden.writerow(prvnidensedmice)

# Maximální průtok
with open("vstup.csv", encoding="utf-8") as csvinfile:
	reader = csv.reader(csvinfile, delimiter = ",")
	maxprutok=max(reader, key=lambda row: float(row[5]))
	print("Toto je den s maximálním průtokem")
	print(maxprutok)
# Minimální průtok
with open("vstup.csv", encoding="utf-8") as csvinfile:
	reader = csv.reader(csvinfile, delimiter = ",")
	minprutok=min(reader, key=lambda row: float(row[5]))
	print("Toto je den s minimálním průtokem")
	print(minprutok)
