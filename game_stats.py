
class GameStats():
	def __init__(self, ai_settings):

		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		self.high_score = 0
		self.read(ai_settings)
	def reset_stats(self):
		self.pers_left = self.ai_settings.pers_limit
		self.score = 0
		self.level = 0
	def read(self,ai_settings):
		with open(ai_settings.textname) as file_object:
			self.high_score = int(file_object.read())
			
