import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
	"""A class to manage the ship"""
	def __init__(self, ai_game):
		"""Initializes the ship and manages its starting positions"""
		super().__init__()#so you can use the super classes' attributes
		self.screen=ai_game.screen
		self.screen_rect=ai_game.screen.get_rect()
		self.setting=ai_game.settings#dont have to import settings, just use the main argument which would have that imported in

		#Load the ship image and get its rect.
		self.image= pygame.image.load('data/images/ship.bmp') #image then dot then the command
		self.rect= self.image.get_rect()
		#Start each new ship at the bottom center of the screen
		self.rect.midbottom=self.screen_rect.midbottom
		#movement flag
		self.moving_right= False
		self.moving_left= False
		self.moving_up= False
		self.moving_down= False
		#stores a decimal number for the hortizontal place of the ship
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)

	def blitme(self):
		"""draw the ship at its current position"""
		self.screen.blit(self.image, self.rect) #first argument is the object, second argument is the rect of the object
	def update_movement(self):
		"""makes the movement flag result in movement of the ship for continuous movement when holding the key"""
		#Updates the ship's x value, not the rect. 
		if self.moving_right and self.rect.right< self.screen_rect.right:
		 #right and left have only x values so its a good reference: 
		 #top and bottom utilise only y values so we can use origin for moving up as when you move down y increases
			self.x+=self.setting.ship_speed
		if self.moving_left and self.rect.left> 0:
			self.x-=self.setting.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.y-=self.setting.ship_speed
		if self.moving_down and self.rect.bottom< self.screen_rect.bottom:
			self.y+=self.setting.ship_speed

		self.rect.x=self.x
		self.rect.y=self.y
	def center_ship(self):
		"""Resets the ship position to the midbottom"""
		self.rect.midbottom=self.screen_rect.midbottom
		self.rect.bottom=self.screen_rect.bottom
		self.y= float(self.rect.y)
		self.x = float(self.rect.x)