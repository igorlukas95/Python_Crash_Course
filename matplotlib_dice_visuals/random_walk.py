from random import choice

class RandomWalk():
	#Klasa przeznaczona do wygenerowania błędu kroczenia losowego
	def __init__(self,num_points=5000):
		#Inicjalizacja atrybutów błądzenia
		self.num_points = num_points
		#punkt początkowy ma współrzędne(0,0)
		self.x_values = [0]
		self.y_values = [0]


		#Wygenerowanie wszytskich punktów dla błądzenia losowego
		#wykonywanie kroków aż do osiągniecia oczekiwanej liczby punktów
		while len(self.x_values)< self.num_points:
			#Ustalenie kierunku oraz odległości do pokonywania w tym kierunku
			x_direction = choice([1,-1])
			x_distance = choice([0,1,2,3,4,5,6,7,8])
			x_step = x_direction*x_distance

			y_direction = choice([1,-1])
			y_distance = choice([0,1,2,3,4,5,6,7,8])
			y_step = y_direction*y_distance

			#odrzucenie ruchów które prowadzą donikąd
			if x_step == 0 and y_step == 0:
				continue
			#Ustalenie następnych wartości X i Y
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step
			self.x_values.append(x)
			self.y_values.append(y)