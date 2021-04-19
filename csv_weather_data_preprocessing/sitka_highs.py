import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#Pobranie temperatur maksymalnych z pliku i dat
	dates, highs=[], []
	for row in reader:
		current_date = datetime.strptime(row[2],"%Y-%m-%d")
		high = int(row[5])
		dates.append(current_date)
		highs.append(high)
	#print(highs)
	#print(dates)
#Dane do wykresy
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red')
#Formatowanie wykresu
ax.set_title("Najwyższa temperatura dnia, rok 2018",fontsize=24)
ax.set_xlabel("",fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura [F]",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
plt.show()