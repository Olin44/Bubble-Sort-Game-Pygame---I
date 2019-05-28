import pygame
from game1v2.Resize import Resize

class Button(pygame.sprite.Sprite):
    def __init__(self, key, position, light_position, scale):
        super().__init__()
        self.key = key
        self.button_position = position
        self.button_light_position = light_position
        self.image_off, self.size_off = Resize(pygame.image.load('./graphics/button_' + self.key + '.png'), scale).resize()
        self.size = self.size_off
        self.rect_off = pygame.Rect(self.button_position[0], self.button_position[1], self.size[0], self.size[1])
        self.image_on, self.size_on = Resize(pygame.image.load('./graphics/button_' + self.key + '_light.png'),
                                             scale).resize()
        self.rect_on = pygame.Rect(self.button_light_position[0], self.button_light_position[1], self.size[0], self.size[1])
        self.rect = self.rect_off
        self.image = self.image_off

    def light_on(self):
        self.rect = self.rect_on
        self.image = self.image_on

    def light_off(self):
        self.rect = self.rect_off
        self.image = self.image_off

    def __str__(self):
        return f"Key {self.key}, postion: {self.button_position}, light postion: {self.button_light_position}, "
