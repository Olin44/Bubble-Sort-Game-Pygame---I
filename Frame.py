import pygame
from game1v2.Resize import Resize

class Frame(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        path = './graphics/frame.png'
        self.image, self.size = Resize(pygame.image.load(path)).resize()
        self.rect = self.image.get_rect()
        self.position = (269, 91)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def frame_surface(self):
        return self.image
