import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet"""

	def __init__(self, ai_game):
		"""Initializes the alien and its starting position"""
		super().__init__()
		self.screen=ai_game.screen
		self.settings= ai_game.settings

		#Load the alien image and set its rect attribute
		self.image= pygame.image.load('data/images/alien.bmp')
		self.rect=self.image.get_rect()

		#Start each new alien near the top left of the screen
		self.rect.x= self.rect.width # this means the bottom left of the image will be at the origin
		self.rect.y= self.rect.height

		#Store the alien's exact horizontal position
		self.x= float(self.rect.x)
		#Alien settings


	def update(self):
		"""Move the alien to the right or left"""
		self.x+= (self.settings.alien_speed * 
			      		self.settings.fleet_direction)
		self.rect.x= self.x

	def check_edges(self):
		"""Check if an alien instance has hit the edges of the screen"""
		screen_rect= self.screen.get_rect()

		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

         #the right most of the alien instance