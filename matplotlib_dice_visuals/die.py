from random import randint
class Die():
	#Klasa przedstawiająca pojedynczą kość do gry
	def __init__(self,num_sides=6):
		#Przyjecie zalozenia ze kosc do gry ma postac szescianu
		self.num_sides = num_sides
	def roll(self):
		#Zwrot wartosci z zakresu od 1 do liczby scian kostki do gry
		return randint(1,self.num_sides)