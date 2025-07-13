import pygame as pg

class Mode:
    """Class for difficulty selection buttons."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Button settings
        self.width, self.height = 200, 50
        self.button_spacing = 100

        self.text_color = (0, 0, 0)
        self.easy_button_color = (124, 179, 66)
        self.normal_button_color = (245, 127, 23)
        self.hard_button_color = (191, 54, 12)

        self.font = pg.font.Font('fonts/pixel_sonic.ttf', 30)

        # Create buttons
        self.easy_button = pg.Rect(0, 0, self.width, self.height)
        self.normal_button = pg.Rect(0, 0, self.width, self.height)
        self.hard_button = pg.Rect(0, 0, self.width, self.height)

        self.total_width = 3 * self.width + 2 * self.button_spacing
        self.start_x = self.screen_rect.centerx - self.total_width // 2
        self.center_y = self.screen_rect.centery

        self.easy_button.topleft = (self.start_x, self.center_y)
        self.normal_button.topleft = (self.start_x + self.button_spacing + self.width, self.center_y)
        self.hard_button.topleft = (self.start_x + 2 * (self.button_spacing + self.width), self.center_y)

        # Prepare button texts
        self.easy_button_text = self.prep_msg('Easy', self.easy_button)
        self.normal_button_text = self.prep_msg('Normal', self.normal_button)
        self.hard_button_text = self.prep_msg('Hard', self.hard_button)

    def prep_msg(self, msg, button):
        """Render text and center it on the button."""
        msg_image = self.font.render(msg, True, self.text_color)
        msg_image_rect = msg_image.get_rect()
        msg_image_rect.center = button.center
        return msg_image, msg_image_rect

    def draw_all_buttons(self):
        """Draw all difficulty buttons and their text."""
        # Easy
        self.screen.fill(self.easy_button_color, self.easy_button)
        self.screen.blit(self.easy_button_text[0], self.easy_button_text[1])

        # Normal
        self.screen.fill(self.normal_button_color, self.normal_button)
        self.screen.blit(self.normal_button_text[0], self.normal_button_text[1])

        # Hard
        self.screen.fill(self.hard_button_color, self.hard_button)
        self.screen.blit(self.hard_button_text[0], self.hard_button_text[1])