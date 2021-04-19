import sys

import pygame
from rakietka import Ship
from settings import Settings

class Rocket:
	"""Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry"""
	def __init__(self):
		"""Inicjalizacja gry i utworzenie zasobów"""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((1200,800))
		pygame.display.set_caption("Rakieta")
		self.ship = Ship(self)


	def run_game(self):
		"""Rozpoczęcie głównej pętli gry"""
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()


	def _check_events(self):
		#Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
	def _check_keydown_events(self,event):
		""" Reakcja na nacisniecie klawisza"""
		if event.key == pygame.K_RIGHT:
			#Przesunięcie statku w prawą stronę
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			#Przesunięcie statku w lewą stronę
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			#Przesunięcie statku w lewą stronę
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			#Przesunięcie statku w lewą stronę
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
	def _check_keyup_events(self,event):
		""" Reakcja na puszczenie klawisza""" 
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
	def _update_screen(self):
		#Odświeżanie ekranu w trakcie każdej pętli iteracji
		self.screen.fill((230,230,230))
		self.ship.blitme()

		#Wyswietlanie ostatnio zmodyfikowanego ekranu
		pygame.display.flip()
if __name__ == '__main__':
	#Utworzenie egzemplarza gry i jej uruchomienie
	ai = Rocket()
	ai.run_game()