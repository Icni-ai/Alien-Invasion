import sys
import pygame as pg
from settings import Settings


class AlienInvasion:
    """Класс для управлением ресурсами и поведением игры"""
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption(self.settings.caption)

    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            pg.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()