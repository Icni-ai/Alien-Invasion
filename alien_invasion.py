import sys
import pygame as pg
from settings import Settings
from ship import Ship


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


    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()


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
        if event.key == pg.K_a:
            self.ship.moving_left = True
        elif event.key == pg.K_d:
            self.ship.moving_right = True
        if event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pg.K_a:
            self.ship.moving_left = False
        elif event.key == pg.K_d:
            self.ship.moving_right = False

    
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.bltime()
            
            pg.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()