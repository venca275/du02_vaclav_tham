import csv
from os import linesep
with open("vstup.csv", encoding="utf-8") as csvinfile,\
	open("vystup_7dni.csv", "w", encoding="utf-8") as csvoutfile:
	# Vytvoříme proměnnou `reader` držící objekt pro čtení z `csvinfile`
	reader = csv.reader(csvinfile, delimiter = ",")
	# Vytvoříme proměnnou `writer` držící objekt pro zápis do `csvoutfile`
	writer = csv.writer(csvoutfile)
	
	sedmiprum = 0
	cisloradky=0
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
		
	