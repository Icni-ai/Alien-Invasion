import sys
import pygame as pg
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Класс для управлением ресурсами и поведением игры"""
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pg.display.set_caption(self.settings.caption)

        image = pg.image.load('images/icon.png')
        pg.display.set_icon(image)

        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()


    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()



    def _check_events(self):
        """Кнопка выхода из окна"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)


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
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.bltime()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()


            pg.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()