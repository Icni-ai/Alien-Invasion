import pygame as pg


class Ship:
    """Класс для управление кораблем"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen # Перенимаем аттрибут screen с основного класса игры, где уже создано окно
        self.screen_rect = ai_game.screen.get_rect() # Получаем инфорамицю о окне и присваиеваем переменной

        self.image = pg.image.load('images/space_ship.png') # Загружаем картинку
        self.image = pg.transform.scale(self.image, (100, 100)) # Задаем рамер картинки
        self.rect = self.image.get_rect() # Получаем информацию о картинке и присваиеваем переменной

        self.rect.midbottom = self.screen_rect.midbottom # Спавним корабль в нижней части экрана по середине
    
    def bltime(self):
        self.screen.blit(self.image, self.rect)