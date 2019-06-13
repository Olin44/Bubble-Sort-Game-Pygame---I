import pygame
from Resize import Resize

class Frame(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        super().__init__()
        path = './graphics/frame.png'
        self.image, self.size = Resize(pygame.image.load(path), scale).resize()
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])

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

    def frame_surface(self):
        return self.image
