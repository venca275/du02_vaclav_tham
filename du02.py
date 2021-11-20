import csv
from os import linesep
with open("vstup.csv", encoding="utf-8") as csvinfile,\
	open("vystup_7dni.csv", "w", encoding="utf-8") as csvoutfile:
	# Vytvoříme proměnnou `reader` držící objekt pro čtení z `csvinfile`
	reader = csv.reader(csvinfile, delimiter = ",")
	# Vytvoříme proměnnou `writer` držící objekt pro zápis do `csvoutfile`
	writer = csv.writer(csvoutfile)
	
	sedmiprum = 0
	cisloradky=-1
	for row in reader:		# Čteme jednotlivé řádky z `reader`u, v `row` máme seznam buněk daného řádku
		cisloradky= cisloradky + 1
		sedmdni= cisloradky % 7
		try:
				sedmiprum = sedmiprum + float(row[5])		# Kratší forma zápisu
				#total = total + int(row[4])	# Delší forma zápisu, dělá to samé, co kratší
		except ValueError:
			pass	
		if sedmdni == 0:
			sedmiprum=sedmiprum/7
			formatted_string="{:.4f}".format(sedmiprum)
			row[5]=float(formatted_string)
			print(row[0:6])
			sedmiprum=0
with open("vstup.csv", encoding="utf-8") as csvinfile,\
	open("vystup_rok.csv", "w", encoding="utf-8") as csvoutfile:
	# Vytvoříme proměnnou `reader` držící objekt pro čtení z `csvinfile`
	reader = csv.reader(csvinfile, delimiter = ",")
	# Vytvoříme proměnnou `writer` držící objekt pro zápis do `csvoutfile`
	writer = csv.writer(csvoutfile)
with open("vstup.csv", encoding="utf-8") as csvinfile:
	reader = csv.reader(csvinfile, delimiter = ",")
	maxprutok=max(reader, key=lambda row: float(row[5]))
	print(maxprutok)
with open("vstup.csv", encoding="utf-8") as csvinfile:
	reader = csv.reader(csvinfile, delimiter = ",")
	minprutok=min(reader, key=lambda row: float(row[5]))
	print(minprutok)
