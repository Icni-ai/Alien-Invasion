class GameStat:
    """Track statistics for the game."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings

        # Initialize dynamic stats
        self.reset_stats()

        # Show mode selection screen
        self.chose_mode_showed = False

        # Game is inactive at start
        self.game_active = False

        # Load high score from file
        try:
            with open('high_score.txt', 'r') as f:
                self.high_score = int(f.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0

    def reset_stats(self):
        """Reset stats for a new game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.wave = 1