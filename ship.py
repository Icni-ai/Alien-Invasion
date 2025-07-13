import pygame as pg


class Ship:
    """Class for controlling the player's ship."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load and scale ship image
        self.image = pg.image.load('images/space_ship.png')
        self.image = pg.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()

        # Start ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Store ship's exact horizontal position as float
        self.x = float(self.rect.x)

    def update(self):
        """Update ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def bltime(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the bottom of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)