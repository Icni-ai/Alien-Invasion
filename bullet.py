import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class representing a single bullet."""

    def __init__(self, ai_game):
        super().__init__()  # Initialize parent Sprite class
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet rectangle at ship's midtop
        self.rect = pg.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet's vertical position as float for smooth movement
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self):
        """Draw bullet as a rectangle."""
        pg.draw.rect(self.screen, self.color, self.rect)