import pygame
from game1v2.Resize import Resize


class Letter(pygame.sprite.Sprite):
    def __init__(self, key, x):
        super().__init__()
        self.key = key
        path = './graphics/letter_' + key + '.png'
        self.image, self.size = Resize(pygame.image.load(path)).resize()
        self.position = (x, 91)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def __str__(self):
        return f"Key {self.key}, postion: {self.position}, light postion: {self.rect}, "
