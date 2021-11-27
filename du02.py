import csv
from os import linesep
from datetime import datetime, timedelta
try:
	with open("vstup.csv", encoding="utf-8") as csvinfile,\
		open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile, \
		open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csvoutfile1:
		# Vytvoříme proměnnou reader držící objekt pro čtení
		reader = csv.reader(csvinfile, delimiter = ",")
		# Vytvoříme proměnnou writertyden, writerrok, držící objekt pro zápis
		writertyden = csv.writer(csvoutfile)
		writerrok = csv.writer(csvoutfile1)
		# Vytvorime si proměnné
		sedmiprum = 0
		cisloradky= 0
		zbytek = 0
		prumrok = 0
		pocetdnuvroce = 0
		maxdenniprutok=0
		mindenniprutok=float('inf')
		# Cyklus, který projede všechny řádky v souboru
		for row in reader:
			try:
				denniprum=float(row[5])
			except ValueError:
				print(f"Na řádku {reader.line_num} je chybná hodnota")
			except IndexError:
				print(f"Na řádku {reader.line_num} je nesprávně dlouhé pole")

			# Detekce chyb záporný nebo nulový průtok
			if (denniprum) <= 0:
				print(f"Průtok dne {row[4]}.{row[3]}.{row[2]} je buďto záporný nebo nulový")
						
			# Přiřazení prvního dne v týdnu
			if cisloradky % 7 == 0:
				prvnidensedmice = row
			# Přičte do sedmidenního průměru, denní prumer z aktualni řádky
			# také počítá zbytek			
			sedmiprum = sedmiprum + (denniprum)
			zbytek = zbytek + 1			
			#  Zjístí, že jsme na posledním dni 7 tak vypočte průměr za týden přiřadí do první řádky sedmice, a následně zapíše
			if cisloradky % 7 == 6:
				sedmiprum= sedmiprum/7
				sedmiprum ="{:.4f}".format(sedmiprum)
				prvnidensedmice[5]= sedmiprum
				writertyden.writerow(prvnidensedmice)
				zbytek = 0
				sedmiprum=0
			cisloradky= cisloradky + 1
			
			# Přičte do ročního průměru, denni prumer z aktualni radky
			prumrok = prumrok + (denniprum)
			# Podmínky pro přirazení prvního dne roku do proměnné
			# Podmínka pro první řádku
			if reader.line_num == 1:
				prvnidenroku = row
				pocitanyrok = int(prvnidenroku[2])
			aktualnirok = int(row[2])
			# Podmínka pro zbytek řádek v programu
			if pocitanyrok != aktualnirok:
				prumrok = prumrok / pocetdnuvroce
				prumrok ="{:.4f}".format(prumrok)
				prvnidenroku[5] = prumrok
				writerrok.writerow(prvnidenroku)
				prumrok=0
				pocetdnuvroce=0
				prvnidenroku=row
				pocitanyrok = int(prvnidenroku[2])

			# Maximální denní průtok
			if (denniprum) > float(maxdenniprutok):
				maxhodnoty=row
				maxdenniprutok = denniprum
			# Minimální denní průtok
			if  (denniprum) < float(mindenniprutok):
				minhodnoty=row
				mindenniprutok = denniprum
			
			pocetdnuvroce = pocetdnuvroce + 1
			# Konec cyklu
		
		# Výpočet prumeru a vypsani, pokud celkový počet řádek není dělitelný 7(mimo cyklus jelikož se udělá pouze jednou na konci)
		if cisloradky % 7 != 0:
			sedmiprum = sedmiprum / zbytek
			sedmiprum = "{:.4f}".format(sedmiprum)
			prvnidensedmice[5] = sedmiprum
			writertyden.writerow(prvnidensedmice)
		# Zapsání posledního roku v tabulce po skončení cyklu(mimo cyklus jelikož se udělá pouze jednou na konci)
		prumrok = prumrok / pocetdnuvroce
		prumrok ="{:.4f}".format(prumrok)
		prvnidenroku[5] = prumrok
		writerrok.writerow(prvnidenroku)


	# Maximální průtok
		print(f"Dne {maxhodnoty[4]}.{maxhodnoty[3]}.{maxhodnoty[2]} byl naměřen nejvyšší denní průtok {maxdenniprutok}")
	# Minimální průtok
		print(f"Dne {minhodnoty[4]}.{minhodnoty[3]}.{minhodnoty[2]} byl naměřen nejnižší denní průtok {mindenniprutok}")
except IOError:
	print("Chybně načtený soubor")