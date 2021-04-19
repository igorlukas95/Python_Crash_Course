from plotly.graph_objs import Bar,Layout
from plotly import offline


from die import Die
#Utworzenie kosci typu D6
die=Die()
#Wykonanie pewnej liczby rzutów i umieszczenie wynikow na liscie
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)
#Analizam wynikow
frequencies = []
for value in range(1,die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
#Wizualizacja wynikow na histogramie
x_values = list(range(1,die.num_sides+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config ={'title':"Wynik"}
y_axis_config = {'title': 'Częstotliwośc występowania wartości'}
my_layout = Layout(title='Wynik wyrzucenia kością D6 1000 razy',xaxis=x_axis_config,yaxis = y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')