import sys
from time import sleep

import pygame as pg

from settings import Settings
from game_stat import GameStat
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


class AlienInvasion:
    """Класс для управлением ресурсами и поведением игры"""
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.stats = GameStat(self)

        pg.display.set_caption(self.settings.caption)

        image = pg.image.load('images/icon.png')
        pg.display.set_icon(image)

        self.bg_image = pg.image.load('images/space.png').convert()
        self.bg_image = pg.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)

        self.bullets = pg.sprite.Group() # Создаем группу снарядов

        self.aliens = pg.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, 'Play')


    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets() # Обновление позиции + проверка 
                self._update_aliens()
            self._update_screen()


    def _check_events(self):
        """Проверка ивентов"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dinamic_settings()
            
            self.stats.reset_stats()
            self.stats.game_active = True

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            pg.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        if event.key == pg.K_a or event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_d or event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_SPACE:
            self._fire_bullet()
        elif event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pg.K_a or event.key == pg.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pg.K_d or event.key == pg.K_RIGHT:
            self.ship.moving_right = False

    
    def _fire_bullet(self):
        """Создание снаряда + проверка на количество снарядов на экране"""
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self.settings.fleet_direction = 1
            self._create_fleet()
            self.settings.increase_speed()


    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        aviable_space_x = self.settings.screen_width - (2 * alien_width)
        numbers_aliens_x = aviable_space_x // (2 * alien_width)

        for row_number in range(3):
            for alien_number in range(numbers_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        for alien in self.aliens:
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _ship_hit(self):
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
        else:
            self.stats.game_active = False
            pg.mouse.set_visible(True)

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        sleep(0.5)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens:
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


    def _update_screen(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.ship.bltime()

        """Рисуем снаряд"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()

        pg.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()