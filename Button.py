import pygame
from game1v2.Resize import Resize


class Button(pygame.sprite.Sprite):
    def __init__(self, key, position, light_postion, light = False):
        super().__init__()
        self.key = key
        self.button_position = position
        self.button_light_position = light_postion
        if light:
            path = './graphics/button_' + self.key + '_light.png'
            self.image, self.size = Resize(pygame.image.load(path)).resize()
            self.rect = (self.button_light_position[0], self.button_light_position[1], self.size[0], self.size[1])
        else:
            path = './graphics/button_' + self.key + '.png'
            self.image, self.size = Resize(pygame.image.load(path)).resize()
            self.rect = pygame.Rect(self.button_position[0], self.button_position[1], self.size[0], self.size[1])

    def on_click(self, function):
        function

    def __str__(self):
        return f"Key {self.key}, postion: {self.button_position}, light postion: {self.button_light_position}, "
