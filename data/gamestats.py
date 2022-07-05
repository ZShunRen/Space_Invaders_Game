class GameStats:
	"""Track statistics for Alien Invasion"""

	def __init__(self, ai_game):
		"""Initializes statistics"""
		self.settings = ai_game.settings
		self.reset_stats()
		#Start Alien Invasion in an inactive state
		self.game_active= False
		filename='high_score.txt'
		with open(filename, 'r') as object:
			all_time=object.read()
		self.high_score=int(all_time)  #High score should never be reset

	def reset_stats(self):
		"""Initializes stats that can be used during the game"""
		self.ships_left= self.settings.ships_limit
		self.score= 0
		self.level= 1