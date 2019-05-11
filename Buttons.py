import pygame
from game1v2.Resize import Resize


class Buttons(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "".join(str(sprite)for sprite in self.sprites())

