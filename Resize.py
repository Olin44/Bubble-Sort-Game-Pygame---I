import pygame


class Resize:
    def __init__(self, img):
        self.img = img
        self.size = img.get_size()
        self.size = int(self.size[0] / 2), int(self.size[1] / 2)
        self.img = pygame.transform.scale(self.img, self.size)

    def resize(self):
        return self.img, self.size
