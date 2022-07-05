class Settings:
	"""A class to store all the settings for the Alien Invasion"""

	def __init__(self):
		"""Initializes the games settings"""
		# Screen settings
		self.screen_width=1920
		self.screen_height=1080
		self.bg_color=(230, 230, 230)# 255 is the max value for any rgb
		#ship settings
		self.ship_speed= 2.5
		self.ships_limit= 3
		#bullet settings
		self.bullet_speed= 2.0 #travels slower than the ship if ship is at 1.5
		self.bullet_width= 3
		self.bullet_height= 15
		self.bullet_color= (60, 60, 60)
		self.bullets_allowed= 3
#alien settings
		self.alien_speed= 0.4
		self.fleet_drop_speed= 5
		self.speedup_scale= 1.1
		self.score_scale= 1.5

		self.initialize_dynamic_settings()
		self.target_direction= 1
	def initialize_dynamic_settings(self):
		"""Initializes settings that change throughout the game to make it more challenging"""
		self.ship_speed= 2.5
		self.bullet_speed= 2.0
		self.alien_speed= 1.0
		#fleet direction of 1 indicates going to the right, -1 to the left
		self.fleet_direction= 1
		#Scoring
		self.alien_points= 50 #the amount of points one alien gives
	def increase_speed(self):
		"""Increases the movement speed of the game by multiplying initial value by scale and alien point values"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points *self.score_scale)
		print(self.alien_points)