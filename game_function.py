import pygame
import sys
from bullet import Bullet
from alien import Alien





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



def check_events(ai_settings, screen, personazh, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()				
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,personazh,bullets, screen, ai_settings)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,personazh)				
 			
def update_screen(ai_settings, screen, personazh, bullets,aliens):
	screen.fill(ai_settings.bg_color)
	personazh.blitme()
	aliens.draw(screen)
	for bullet in bullets.sprites():
 		bullet.draw_bullet()
	pygame.display.flip()
	
def update_bullets(bullets,aliens):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
		#if bullet.rect.centerx >= 1024:
			bullets.remove(bullet)
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)			










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
	number_rows = get_number_rows(ai_settings, personazh.rect.height,alien.rect.height)
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)


def check_fleet_edges(ai_settings, aliens,alien):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens,alien)
			print(alien.check_edges())
			break
def change_fleet_direction(ai_settings, aliens,alien):
	
	for alien in aliens.sprites():
		ai_settings.fleet_direction *= -1
		alien.rect.y += ai_settings.fleet_drop_speed

		


def update_aliens(aliens,ai_settings,alien):
	check_fleet_edges(ai_settings, aliens,alien)
	aliens.update()