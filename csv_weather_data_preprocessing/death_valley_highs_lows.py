import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)


	#Pobranie temperatur maksymalnych z pliku i dat
	dates, highs, lows=[], [], []
	for row in reader:
		current_date = datetime.strptime(row[2],"%Y-%m-%d")
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Brak danych dla {current_date}.")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
	#print(highs)
	#print(dates)
#Dane do wykresy
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#Formatowanie wykresu
ax.set_title("Najwyższa i najniższa temperatura dnia, rok 2018",fontsize=24)
ax.set_xlabel("",fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura [F]",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
ax.set_ylim([0,120])
plt.show()