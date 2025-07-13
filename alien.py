import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing a single alien."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load and scale alien image
        self.image = pg.image.load('images/alien.png')
        self.image = pg.transform.scale(self.image, (90, 70))
        self.rect = self.image.get_rect()

        # Start alien near the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact horizontal position as float
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move alien right or left."""
        self.x += ((self.settings.alien_speed / 10) * self.settings.fleet_direction)
        self.rect.x = self.x