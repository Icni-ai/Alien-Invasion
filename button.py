import pygame as pg

class Button:
    """Class for a simple UI button."""

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Button settings
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.font = pg.font.Font('fonts/pixel_sonic.ttf', 30)

        # Create button rect and center it
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare button text
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Render text and center it on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw button and text to the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)