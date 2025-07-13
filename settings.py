class Settings:
    """Класс для хранения всех настроек"""
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.caption = 'Alien Invasion'

        # Параметры скорости управляемого корабля
        self.ship_limit = 3
        
        # Параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 3

        # Параметры пришельцев
        self.fleet_drop_speed = 50

        self.speedup_scale = 1.1

        self.initialize_dinamic_settings()


    def initialize_dinamic_settings(self):
        self.ship_speed = 1.2
        self.bullet_speed = 1
        self.alien_speed = 2
        # fleet_direction = 1 обозначает движение вправо; -1 - влево
        self.fleet_direction = 1


    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale