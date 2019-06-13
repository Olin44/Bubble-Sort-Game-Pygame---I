import pygame
from Resize import Resize


class Letter(pygame.sprite.Sprite):
    def __init__(self, key, x, scale):
        super().__init__()
        self.key = key
        path = './graphics/letter_' + key + '.png'
        self.image, self.size = Resize(pygame.image.load(path), scale).resize()
        self.position = (x, 91)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def get_position_x(self):
        return self.rect[0]

    def get_position_y(self):
        return self.rect[1]

    def get_coordinate_xy(self):
        return self.rect[0], self.rect[1]

    def set_position_x(self, x):
        self.rect[0] = x

    def set_position_y(self, y):
        self.rect[0] = y

    def __str__(self):
        return f"Key {self.key}, postion: {self.position}, light postion: {self.rect}, "
