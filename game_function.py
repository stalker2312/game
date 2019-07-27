import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep




def check_keyup_events(event,personazh):

	if event.key == pygame.K_RIGHT:
 		personazh.moving_right = False
	if event.key == pygame.K_LEFT:
 		personazh.moving_left = False
	if event.key == pygame.K_DOWN:
 		personazh.moving_down = False
	if event.key == pygame.K_UP:
 		personazh.moving_up = False	


			

def check_keydown_events(event,personazh,bullets, screen, ai_settings):
	if event.key == pygame.K_RIGHT:
		personazh.moving_right = True
	if event.key == pygame.K_LEFT:
 		personazh.moving_left = True
	if event.key == pygame.K_DOWN:
 		personazh.moving_down = True
	if event.key == pygame.K_UP:
 		personazh.moving_up = True
	elif event.key == pygame.K_SPACE:
		if(len(bullets)<ai_settings.bullets_allowed):
			new_bullet = Bullet(ai_settings, screen, personazh)
			bullets.add(new_bullet)
	elif event.key == pygame.K_q:
		sys.exit			



def check_events(ai_settings, screen, personazh, bullets,stats,play_button,aliens,alien,sb):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			with open(ai_settings.textname, 'w') as file_object:
				file_object.write(str(stats.high_score))
			sys.exit()				
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,personazh,bullets, screen, ai_settings)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,personazh)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,personazh,play_button,mouse_x,mouse_y,aliens,bullets,alien,sb)
def check_play_button(ai_settings,screen,stats,personazh,play_button,mouse_x,mouse_y,aliens,bullets,alien,sb):
	
	button_cliked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_cliked and not stats.game_active:
		stats.game_active = True
		stats.game_active = True
		
		aliens.empty()
		bullets.empty()
		ai_settings.initialize_dynamic_settings()
		check_fleet_edges(ai_settings,aliens,alien)
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		sb.pre_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_pers()
		



 			
def update_screen(ai_settings, screen, personazh, bullets,aliens,play_button,stats,sb):
	screen.fill(ai_settings.bg_color)
	personazh.blitme()
	aliens.draw(screen)
	sb.show_score()
	if not stats.game_active:
		play_button.draw_button()
	for bullet in bullets.sprites():
 		bullet.draw_bullet()
	pygame.display.flip()

	
def update_bullets(ai_settings,screen,personazh,bullets,aliens,sb,stats):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
		#if bullet.rect.centerx >= 1024:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings, screen, personazh, aliens, bullets,sb,stats)	

def check_bullet_alien_collisions(ai_settings, screen, personazh, aliens, bullets,sb,stats):
	#Обработка коллизий пуль с пришельцами.
	# Удаление пуль и пришельцев, участвующих в коллизиях.
	print(len(aliens))
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
	# Уничтожение существующих пуль и создание нового флота.
		bullets.empty()
		create_fleet(ai_settings, screen, aliens,personazh)
		ai_settings.increase_speed()
		stats.level += 1
		sb.prep_level()
	if collisions:
		for aliens in collisions.values():
			sb.stats.score =  sb.stats.score + (ai_settings.alien_points * len(aliens))
			sb.pre_score()
			check_high_score(stats, sb,ai_settings)



def create_alien(ai_settings, screen, aliens, alien_number,row_number):
	alien = Alien(ai_settings, screen)
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	aliens.add(alien)

def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x	

def get_number_rows(ai_settings, personazh_height, alien_height):
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - personazh_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def create_fleet(ai_settings, screen, aliens,personazh):
	"""Создает флот пришельцев."""
 # Создание первого ряда пришельцев.
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings,personazh.rect.height,alien.rect.height)
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)


def check_fleet_edges(ai_settings, aliens,alien):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens,alien)
			
			break
def change_fleet_direction(ai_settings, aliens,alien):
	
	for alien in aliens.sprites():
		ai_settings.fleet_direction *= -1
		alien.rect.y += ai_settings.fleet_drop_speed

def pers_hit(ai_settings, stats, screen, personazh, aliens, bullets,sb):
	if stats.pers_left > 0:
		stats.pers_left -= 1
		sb.prep_pers()
		print(stats.pers_left)

	 # Очистка списков пришельцев и пуль.
		aliens.empty()
		bullets.empty()

	 # Создание нового флота и размещение корабля в центре.
		create_fleet(ai_settings, screen, aliens,personazh)
		personazh.center_pers()

	 # Пауза.
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)




def update_aliens(ai_settings, stats, screen, personazh, aliens, bullets,alien,sb):
	check_fleet_edges(ai_settings, aliens, alien)
	aliens.update()
	if pygame.sprite.spritecollideany(personazh, aliens):
		pers_hit(ai_settings,stats,screen,personazh,aliens,bullets,sb)
	check_aliens_bottom(ai_settings, stats, screen, personazh, aliens, bullets,sb)

def check_aliens_bottom(ai_settings, stats, screen, personazh, aliens, bullets,sb):
	#Проверяет, добрались ли пришельцы до нижнего края экрана.
	
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
 		if alien.rect.bottom >= screen_rect.bottom - 20:
 # Происходит то же, что при столкновении с кораблем.
 			pers_hit(ai_settings, stats, screen, personazh, aliens, bullets,sb)
 			break
def check_high_score(stats, sb, ai_settings):
#Проверяет, появился ли новый рекорд.""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()			