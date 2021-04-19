import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	for index, column in enumerate(header_row):
		print(index,column)
	#Pobranie temperatur maksymalnych z pliku i dat
	dates, rains=[], []
	for row in reader:
		current_date = datetime.strptime(row[2],"%Y-%m-%d")
		try:
			rain=float(row[3])
		except ValueError:
			print(f"Nie można odnaleźć wartosci dla dnia{current_date}")
		else:
			dates.append(current_date)
			rains.append(rain)
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,rains,c='red',alpha=0.5)
#Formatowanie wykresu
ax.set_title("Opady dnia, rok 2018",fontsize=24)
ax.set_xlabel("",fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Opady [mm]",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
plt.show()