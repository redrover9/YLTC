class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        self.ship_speed = 5.0
        self.ship_limit = 3
        self.bullet_speed = 7.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (195, 195, 195)
        self.bullets_allowed = 5
        self.alien_speed = 3.5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
        self.speedup_scale = 1.25
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 0.75
        self.bullet_speed = 1.0
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_points = 50
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
