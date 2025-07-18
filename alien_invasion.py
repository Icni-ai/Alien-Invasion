import sys
from time import sleep

import pygame as pg

from settings import Settings
from game_stat import GameStat
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from mode import Mode
from scoreboard import Scoreboard
from sounds import Sounds


class AlienInvasion:
    """Main class for managing game resources and behavior."""

    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.sounds = Sounds()
        self.stats = GameStat(self)

        pg.display.set_caption(self.settings.caption)
        image = pg.image.load('images/icon.png')
        pg.display.set_icon(image)

        self.bg_image = pg.image.load('images/space.png').convert()
        self.bg_image = pg.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()  # Bullet group
        self.aliens = pg.sprite.Group()   # Alien group

        self.mode_buttons = Mode(self)
        self.sb = Scoreboard(self)

        self._create_fleet()
        self.play_button = Button(self, 'Play')


    def run_game(self):
        """Main game loop."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()


    def _check_events(self):
        """Event handling."""
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
                if not self.stats.chose_mode_showed:
                    self._check_play_button(mouse_pos)
                elif self.stats.chose_mode_showed and not self.stats.game_active:
                    self._select_mode_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Handle Play button click."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.chose_mode_showed:
            self.settings.initialize_dinamic_settings()
            self.stats.reset_stats()
            self.stats.chose_mode_showed = True
            self.sb.prep_score()
            self.sb.prep_wave()
            self.sb.prep_hearts()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()


    def _select_mode_button(self, mouse_pos):
        """Handle difficulty selection buttons."""
        easy_button_clicked = self.mode_buttons.easy_button.collidepoint(mouse_pos)
        normal_button_clicked = self.mode_buttons.normal_button.collidepoint(mouse_pos)
        hard_button_clicked = self.mode_buttons.hard_button.collidepoint(mouse_pos)

        if easy_button_clicked:
            self.stats.game_active = True

        if normal_button_clicked:
            self.settings.alien_speed = self.settings.alien_normalmode_speed
            self.stats.game_active = True
            self.settings.alien_points = 60

        if hard_button_clicked:
            self.settings.alien_speed = self.settings.alien_hardmode_speed
            self.stats.game_active = True
            self.settings.alien_points = 70

        if self.stats.game_active:
            pg.mouse.set_visible(False)
            self.sounds.bg_sound.play(-1)


    def _check_keydown_events(self, event):
        """Handle keydown events."""
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
        """Handle keyup events."""
        if event.key == pg.K_a or event.key == pg.K_LEFT:
            self.ship.moving_left = False

        elif event.key == pg.K_d or event.key == pg.K_RIGHT:
            self.ship.moving_right = False


    def _fire_bullet(self):
        """Create bullet if allowed and play sound."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.sounds.shoot_sound.play()


    def _update_bullets(self):
        """Update bullet positions and check collisions."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Check bullet-alien collisions and update score."""
        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            self.sounds.collide_sound.play()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self.settings.fleet_direction = 1
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.wave += 1
            self.sb.prep_wave()
            self.sounds.wave_sound.play()


    def _update_aliens(self):
        """Update alien positions and check for collisions with ship or bottom."""
        self._check_fleet_edges()
        self.aliens.update()

        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()


    def _create_fleet(self):
        """Create a fleet of aliens."""
        alien = Alien(self)
        alien_width = alien.rect.width
        aviable_space_x = self.settings.screen_width - (2 * alien_width)
        numbers_aliens_x = aviable_space_x // (2 * alien_width)

        for row_number in range(3):
            for alien_number in range(numbers_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Create a single alien and add to the fleet."""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        """Check if any alien reached the edge and change direction."""
        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the fleet and reverse its direction."""
        for alien in self.aliens:
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _ship_hit(self):
        """Handle ship being hit by alien."""
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.sb.prep_hearts()
            self.sounds.ship_hit_sound.play()
        else:
            self.stats.game_active = False
            self.stats.chose_mode_showed = False
            pg.mouse.set_visible(True)
            self.sounds.bg_sound.stop()
            self.sounds.game_over_sound.play()

        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()
        sleep(0.5)


    def _check_aliens_bottom(self):
        """Check if any alien reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens:
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


    def _update_screen(self):
        """Draw all game elements on the screen."""
        self.screen.blit(self.bg_image, (0, 0))
        self.ship.bltime()

        # Draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw aliens
        self.aliens.draw(self.screen)

        # Draw score if game is active
        if self.stats.game_active:
            self.sb.show_score()

        # Draw Play button if mode selection is not shown
        if not self.stats.chose_mode_showed:
            self.play_button.draw_button()

        # Draw mode selection buttons if needed
        if self.stats.chose_mode_showed and not self.stats.game_active:
            self.mode_buttons.draw_all_buttons()

        pg.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()