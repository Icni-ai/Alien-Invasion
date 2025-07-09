import pygame as pg


class Ship:
    """Класс для управление кораблем"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen # Перенимаем аттрибут screen с основного класса игры, где уже создано окно
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() # Получаем инфорамицю о окне и присваиеваем переменной

        self.image = pg.image.load('images/space_ship.png') # Загружаем картинку
        self.image = pg.transform.scale(self.image, (70, 70)) # Задаем рамер картинки
        self.rect = self.image.get_rect() # Получаем информацию о картинке и присваиеваем переменной

        self.rect.midbottom = self.screen_rect.midbottom # Спавним корабль в нижней части экрана по середине

        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)


    def update(self):
        # Возвращает координату x правого края прямоугольника и сравнивает с координатами правого края экрана
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x


    def bltime(self):
        self.screen.blit(self.image, self.rect)