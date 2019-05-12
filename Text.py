import pygame
from game1v2.Resize import Resize


class Text(pygame.Surface):
    def __init__(self, screen, text):
        super().__init__((300, 300))
        self.rect = pygame.Rect(300, 91, 300, 300)
        self.image = pygame.draw.rect(screen, (255,255,255), self.rect)

