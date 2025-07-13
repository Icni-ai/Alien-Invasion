class Settings:
    """Class for storing all game settings."""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.caption = 'Alien Invasion'

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 50

        # Speed and score scaling
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dinamic_settings()
        self.select_mode()

    def initialize_dinamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.2
        self.bullet_speed = 1
        self.alien_speed = 2
        # fleet_direction = 1 means right, -1 means left
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """Increase speed and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def select_mode(self):
        """Set alien speed for different difficulty modes."""
        self.alien_normalmode_speed = self.alien_speed * 1.5
        self.alien_hardmode_speed = self.alien_speed * 2