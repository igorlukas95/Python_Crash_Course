from plotly.graph_objs import Bar,Layout
from plotly import offline


from die import Die
#Utworzenie kosci typu D6 i D10
die_1=Die()
die_2=Die()
die_3=Die()
#Wykonanie pewnej liczby rzutów i umieszczenie wynikow na liscie
results = []
for roll_num in range(5000):
	result = die_1.roll()+die_2.roll()+die_3.roll()
	results.append(result)
#Analizam wynikow
frequencies = []
max_result = die_1.num_sides + die_2.num_sides+die_3.num_sides
for value in range(3,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
#Wizualizacja wynikow na histogramie
x_values = list(range(3,max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config ={'title':"Wynik",'dtick':1}
y_axis_config = {'title': 'Częstotliwośc występowania wartości'}
my_layout = Layout(title='Wynik wyrzucenia trzema kośćmi D6 5000 razy',xaxis=x_axis_config,yaxis = y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6d6d6.html')