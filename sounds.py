from pygame import mixer

class Sounds:
    def __init__(self):
        self.bg_sound = mixer.Sound('sounds/bg_sound.mp3')

        self.game_over_sound = mixer.Sound('sounds/game_over_sound.mp3')

        self.shoot_sound = mixer.Sound('sounds/shoot_sound.mp3')

        self.collide_sound = mixer.Sound('sounds/collide_sound.mp3')

        self.ship_hit_sound = mixer.Sound('sounds/ship_hit_sound.mp3')

        self.wave_sound = mixer.Sound('sounds/wave_sound.mp3')