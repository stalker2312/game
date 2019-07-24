import pygame
import sys
from settings import Settings
from pers import Perso
import game_function as gf
from pygame.sprite import Group
from alien  import Alien


bullets = Group()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
aliens = Group()
alien = Alien(ai_settings,screen )
personazh = Perso(screen,ai_settings)
gf.create_fleet(ai_settings, screen, aliens,personazh)
def run_game(ai_settings, screen, personazh, bullets, aliens):
 # Инициализирует pygame, settings и объект экрана.
	pygame.init()
	pygame.display.set_caption("Alien Invasion")
	gf.check_events(ai_settings, screen, personazh, bullets)
	personazh.update()
	gf.update_bullets(bullets,aliens)
	gf.update_screen(ai_settings, screen, personazh, bullets,aliens)
	gf.update_aliens(aliens,ai_settings,alien)

	
# Запуск основного цикла игры.
while True:
# При каждом проходе цикла перерисовывается экран.
# Отображение последнего прорисованного экрана.
	run_game(ai_settings, screen, personazh, bullets, aliens)
	
	
    