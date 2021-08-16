class GameStats:
    
    def __init__(self, si_game):
        self.high_score = 0
        self.settings = si_game.settings
        self.reset_stats()
        self.game_active = False
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
