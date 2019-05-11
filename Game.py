import pygame
from game1v2.Resize import Resize
from game1v2.Letters import Letters
from game1v2.Letter import Letter
from game1v2.Frame import Frame
from game1v2.Buttons import Buttons
from game1v2.Button import Button

import random

class Game:
    def __init__(self):
        super().__init__()
        pygame.init()
        self.background_image = pygame.image.load("graphics/chest.png")
        self.background_image, self.size = Resize(self.background_image).resize()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Bubble Sort Game")
        self.letters = Letters()
        self.buttons = Buttons()
        self.frame = Frame()
        self.letters_key = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'N', 'O', 'P', 'R', 'S', 'X', 'Z')
        self.buttons_positions = {'L': (280, 165), 'O': (680, 165), 'R': (380, 165)}
        self.buttons_light_position = {'L': (270, 155), 'O': (670, 155), 'R': (370, 155)}

    def draw_board(self):
        self.screen.blit(self.background_image, (0, 0))
        for num, key in enumerate(random.sample(self.letters_key, 10)):
            self.letters.add(Letter(key, 269 + (num * 50)))
        self.letters.draw(self.screen)
        for key in self.buttons_positions.keys():
            self.buttons.add(Button(key, self.buttons_positions[key], self.buttons_light_position[key]))
        for sprite in self.buttons.sprites():
            print(sprite)
        print(self.buttons)
        self.buttons.draw(self.screen)
        self.screen.blit(self.frame.frame_surface(), (269, 91))
        pygame.display.flip()

    def button_click(self, event, frame):
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.rect.collidepoint(x, y):
                    self.frame = button.on_click()

    def main_loop(self):
        self.draw_board()
        while True:
            self.event_loop()

    # event loop to implements events
    def event_loop(self):
        for event in pygame.event.get():
            print(event)
            self.button_click(event, self.frame)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    # starts the game
    def run(self):
        self.main_loop()


g = Game()

g.run()