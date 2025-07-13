from pygame import mixer

class Sounds:
    """Class for loading and storing game sounds."""

    def __init__(self):
        # Background music
        self.bg_sound = mixer.Sound('sounds/bg_sound.mp3')

        # Game over sound
        self.game_over_sound = mixer.Sound('sounds/game_over_sound.mp3')

        # Shooting sound
        self.shoot_sound = mixer.Sound('sounds/shoot_sound.mp3')

        # Alien collision sound
        self.collide_sound = mixer.Sound('sounds/collide_sound.mp3')

        # Ship hit sound
        self.ship_hit_sound = mixer.Sound('sounds/ship_hit_sound.mp3')

        # Wave complete sound