import pygame
import sys
from pygame.sprite import Sprite
class Perso(Sprite):
	def __init__(self, screen,ai_settings):
		super(Perso, self).__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		self.image = pygame.image.load('img/rocket.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = float(self.screen_rect.centerx)
		self.rect.bottom = float(500)
		float(self.rect.y)
		self.moving_right = False
		self.moving_left = False
		self.moving_down = False
		self.moving_up = False
	def update(self):
	 	if self.moving_right and self.rect.right < self.screen_rect.right :
	 		self.rect.centerx += self.ai_settings.pers_speed
	 	if self.moving_left and self.rect.left > 0:
	 		self.rect.centerx -= self.ai_settings.pers_speed
	 	if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
	 		self.rect.bottom += self.ai_settings.pers_speed
	 	if self.moving_up and self.rect.y > 0:
	 		self.rect.y -= self.ai_settings.pers_speed		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
	def center_pers(self):
		self.center = self.screen_rect.centerx 

			