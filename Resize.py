import pygame


class Resize:
    def __init__(self, img, scale=2):
        self.scale = scale
        self.img = img
        self.size = img.get_size()
        self.size = int(self.size[0] / scale), int(self.size[1] / scale)
        self.img = pygame.transform.scale(self.img, self.size)

    def resize(self):
        return self.img, self.size

    def get_img(self):
        return self.img

    def get_scale(self):
        return self.scale
