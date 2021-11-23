import csv
from os import linesep
with open("vstup.csv", encoding="utf-8") as csvinfile,\
	 open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile, \
	 open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csvoutfile1:
	# Vytvoříme proměnnou `reader` držící objekt pro čtení z `csvinfile`
	reader = csv.reader(csvinfile, delimiter = ",")
	# Vytvoříme proměnnou `writer`, jak pro tydenni prumery tak pro rocni držící objekt pro zápis do `csvoutfile`
	writertyden = csv.writer(csvoutfile)
	writerrok = csv.writer(csvoutfile1)
	# Vytvorime si proměnné sedmiprum(prumer za 7 dni) a promennou cisloradky
	sedmiprum = 0
	cisloradky= 0
	zbytek = 0
	prumrok = 0
	pocetdnuvroce = 0
	max=0
	min=60000
	# Cyklus, který projede všechny řádky v souboru
	for row in reader:		# Čteme jednotlivé řádky z `reader`u, v `row` máme seznam buněk daného řádku
		# Zjišťujeme zda je cisloradky delitelné 7 a skončí dělení nulou, poté přiřadíme aktualní řádku do proměnné
		if cisloradky % 7 == 0:
			prvnidensedmice = row
		
		# Přiřadí do sedmidenního průměru, denní prumer z aktualni řádky
		# také připočítá zbytek + 1, kvůli tomu abychom zajistili správný výpočet pokud by počet řádek nebyl dělitelný 7
		try:
				sedmiprum = sedmiprum + float(row[5])
				zbytek = zbytek + 1		
		except ValueError:
			print("Na řádku je chybná hodnota")
		# Maximální denní průtok
		if float(row[5]) > float(max):
			maxprutok=row
			max = row[5]
		# Minimální denní průtok
		if float(row[5]) < float(min):
			minimalprutok=row
			min = row[5]
		# Přiřadí do prumrok, denni prumer z aktualni radky
		try:
				prumrok = prumrok + float(row[5])		
		except ValueError:
			print("Na řádku je chybná hodnota")
		
		if cisloradky % 7 == 6:
			sedmiprum= sedmiprum/7
			sedmiprum ="{:.4f}".format(sedmiprum)
			prvnidensedmice[5]= sedmiprum
			writertyden.writerow(prvnidensedmice)
			zbytek = 0
			sedmiprum= float(sedmiprum)
			sedmiprum=0
		cisloradky= cisloradky + 1
		
		# Podmínky pro přirazení prvního dne roku do proměnné
		if reader.line_num == 1:
			prvnidenroku = row
			pocitanyrok = int(prvnidenroku[2])
		aktualnirok = int(row[2])
		if pocitanyrok != aktualnirok:
			prumrok = prumrok / pocetdnuvroce
			prumrok ="{:.4f}".format(prumrok)
			prvnidenroku[5] = prumrok
			writerrok.writerow(prvnidenroku)
			prumrok= float(prumrok)
			prumrok=0
			pocetdnuvroce=0
			prvnidenroku=row
			pocitanyrok = int(prvnidenroku[2])
		
		pocetdnuvroce = pocetdnuvroce + 1
	# Výpočet prumeru a vypsani, pokud celkový počet řádek není dělitelný 7
	if cisloradky % 7 != 6:
		sedmiprum = sedmiprum / zbytek
		sedmiprum = "{:.4f}".format(sedmiprum)
		prvnidensedmice[5] = sedmiprum
		writertyden.writerow(prvnidensedmice)
	# Zapsání posledního roku v tabulce po skončení cyklu
	prumrok = prumrok / pocetdnuvroce
	prumrok ="{:.4f}".format(prumrok)
	prvnidenroku[5] = prumrok
	writerrok.writerow(prvnidenroku)

# Maximální průtok
	print("Toto je den s maximálním průtokem")
	print(maxprutok)
# Minimální průtok
	print("Toto je den s minimálním průtokem")
	print(minimalprutok)
