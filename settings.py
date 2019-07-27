class Settings():

	def __init__(self):

		self.screen_width = 1024
		self.screen_height = 500
		self.bg_color = (0,0,100)
		self.pers_speed = 2
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 255, 0, 0
		self.bullets_allowed = 3
		self.alien_speed_factor = -2
		self.fleet_drop_speed = 3
		self.fleet_direction = 1
		self.pers_limit = 3
		self.speedup_scale = 3
		self.textname = 'game.txt'
		self.initialize_dynamic_settings()
	
	def initialize_dynamic_settings(self):
		#Инициализирует настройки, изменяющиеся в ходе игры.
		self.pers_speed = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
        #Увеличивает настройки скорости.
		self.pers_speed *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale	





