class GameStat:
    def __init__(self, ai_game):
        self.settings = ai_game.settings

        self.reset_stats()

        self.chose_mode_showed = False

        self.game_active = False

        try:
            with open('high_score.txt', 'r') as f:
                self.high_score = int(f.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.wave = 1