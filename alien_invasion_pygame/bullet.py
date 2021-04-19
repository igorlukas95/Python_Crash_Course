import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Klasa przeznaczona do zarządzania pociskam wystrzeliwanymi przez gracza"""

	def __init__(self,ai_game):
		"""Utworzenie obiektu pocisku w akutalnym położeniu statku"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color =self.settings.bullet_color

		#Utworzenie pocisku w punkcie (0,0) a następnie zdefiniowanie
		#dla niego odpowiedniego ułożenia
		self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		#Położenie pocisku zdefiniowane jest jako wartość zmiennoprzecinkowa
		self.y = float(self.rect.y)

	def update(self):
		#Poruszanie pociskiem po ekranie
		#Uaktualnienie położenia pocisku
		self.y -= self.settings.bullet_speed
		#Uaktualnienie położenia prostokąta pocisku
		self.rect.y = self.y
	def draw_bullet(self):
		#Wyświetlenie pocisku na ekranie
		pygame.draw.rect(self.screen,self.color,self.rect)

	def Igor(self)