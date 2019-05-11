import pygame
from game1v2.Resize import Resize

class Frame(pygame.sprite.Sprite):
    def __init__(self, x = 269, y = 91):
        super().__init__()
        path = './graphics/frame.png'
        self.image, self.size = Resize(pygame.image.load(path)).resize()
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])

    def frame_surface(self):
        return self.image
