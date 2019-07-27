import pygame
import sys
from settings import Settings
from pers import Perso
import game_function as gf
from pygame.sprite import Group
from alien  import Alien
from game_stats import GameStats
from button import Button


bullets = Group()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
aliens = Group()
stats = GameStats(ai_settings)
alien = Alien(ai_settings,screen )
personazh = Perso(screen,ai_settings)
gf.create_fleet(ai_settings, screen, aliens,personazh)
play_button = Button(ai_settings,screen,'Play')
def run_game(ai_settings, screen, personazh, bullets, aliens,alien,play_button,stats):
 # Инициализирует pygame, settings и объект экрана.
	pygame.init()
	pygame.display.set_caption("Alien Invasion")
	gf.check_events(ai_settings, screen, personazh, bullets,stats,play_button,aliens,alien)
	gf.update_screen(ai_settings, screen, personazh,bullets,aliens,play_button,stats)
	if stats.game_active:
		personazh.update()
		gf.update_aliens(ai_settings, stats, screen, personazh, aliens, bullets,alien)
		gf.update_bullets(ai_settings,screen,personazh,bullets,aliens)
		
	

	
# Запуск основного цикла игры.
while True:
# При каждом проходе цикла перерисовывается экран.
# Отображение последнего прорисованного экрана.
	run_game(ai_settings, screen, personazh, bullets, aliens,alien,play_button,stats)
	
    