import pygame
from Resize import Resize


class Letters(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "".join(str(sprite)for sprite in self.sprites())
