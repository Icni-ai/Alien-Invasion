import pygame as pg


class Scoreboard:
    """Class for displaying and updating game statistics."""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats

        self.text_color = (255, 255, 255)
        self.font_score = pg.font.Font('fonts/pixel_sonic.ttf', 38)
        self.font_high_wave = pg.font.Font('fonts/pixel_sonic.ttf', 30)

        self.prep_score()
        self.prep_high_score()
        self.prep_wave()
        self.prep_hearts()


    def prep_score(self):
        """Prepare the current score image."""
        rounded_score = round(self.stats.score, -1)
        score_str = '{:,}'.format(rounded_score).replace(',', '.')
        self.score_image = self.font_score.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Prepare the high score image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = '{:,}'.format(high_score).replace(',', '.')
        self.high_score_image = self.font_high_wave.render(f'High score: {high_score_str}', True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    
    def prep_wave(self):
        """Prepare the wave image."""
        self.wave_image = self.font_high_wave.render(f'Wave: {self.stats.wave}', True, self.text_color)
        self.wave_image_rect = self.wave_image.get_rect()
        self.wave_image_rect.right = self.score_rect.right
        self.wave_image_rect.top = self.score_rect.bottom + 10


    def prep_hearts(self):
        """Prepare heart images for remaining lives."""
        self.hearts = []
        for heart_number in range(self.stats.ships_left):
            heart_image = pg.image.load('images/heart.png')
            heart_image = pg.transform.scale(heart_image, (60, 50))
            heart_rect = heart_image.get_rect()
            heart_rect.x = 20 + heart_number * 40
            heart_rect.y = 20
            self.hearts.append((heart_image, heart_rect))

    
    def check_high_score(self):
        """Check and update high score if needed."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            with open('high_score.txt', 'w') as f:
                f.write(str(self.stats.high_score))


    def show_score(self):
        """Draw all score elements to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.wave_image, self.wave_image_rect)
        for heart_image, heart_rect in self.hearts:
            self.screen.blit(heart_image, heart_rect)