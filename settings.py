class Settings:
    """Класс для хранения всех настроек"""
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.caption = 'Alien Invasion'

        # Параметры скорости управляемого корабля
        self.ship_speed = 0.6
        
        # Параметры снаряда
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3