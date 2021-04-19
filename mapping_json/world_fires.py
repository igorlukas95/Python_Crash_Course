import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
#Analiza danych
filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
#for index,column in enumerate(header_row):
	#print(index,column)
	mags,lons,lats = [],[],[]
	for row in reader:
		mag = float(row[2])
		lon =float(row[1])
		lat = float(row[0])
		mags.append(mag)
		lons.append(lon)
		lats.append(lat)
print(len(mags))
#Mapa pożarów na ziemi
data = [{
	'type':'scattergeo',
	'lon':lons,
	'lat':lats,
	'marker':{
		'size': [0.06*mag for mag in mags],
		'color':mags,
		'colorscale':'Viridis',
		'reversescale': True,
		'colorbar':{'title':'Siła ognia'},
	},
}]
my_layout = Layout(title="Pożary na świecie")
fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='global_fires.html')
	