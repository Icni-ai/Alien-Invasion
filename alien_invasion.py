import sys
import pygame as pg
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управлением ресурсами и поведением игры"""
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption(self.settings.caption)
        image = pg.image.load('images/icon.png')
        pg.display.set_icon(image)
        self.ship = Ship(self)


    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.bltime()
            
            pg.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()