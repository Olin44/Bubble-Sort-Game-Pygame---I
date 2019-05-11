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
        for num, key in enumerate(random.sample(self.letters_key, 10)):
            self.letters.add(Letter(key, 269 + (num * 50)))
        for key in self.buttons_positions.keys():
            self.buttons.add(Button(key, self.buttons_positions[key], self.buttons_light_position[key]))
        self.update()
        self.screen.blit(self.frame.frame_surface(), (269, 91))
        pygame.display.flip()

    def update(self):
        self.screen.blit(self.background_image, (0, 0))
        self.letters.draw(self.screen)
        self.buttons.draw(self.screen)
        self.screen.blit(self.frame.frame_surface(), (self.frame.rect[0], self.frame.rect[1]))
        pygame.display.flip()

    def move_right(self):
        x, y = self.frame.rect[0], self.frame.rect[1]
        print(x, y)
        if x < 669:
            x += 50
        self.screen.blit(self.frame.frame_surface(), (x, y))
        self.frame.rect[0] = x

    def move_left(self):
        x, y = self.frame.rect[0], self.frame.rect[1]
        print(x, y)
        if x > 269:
            x -= 50
        self.screen.blit(self.frame.frame_surface(), (x, y))
        self.frame.rect[0] = x

    def swap(self):
        x, y = self.frame.rect[0], self.frame.rect[1]
        let_iter = iter(self.letters.sprites())
        print(self.letters)
        for letter in let_iter:
            if letter.position[0] == x:
                let1 = letter
                let2 = next(let_iter)
                let1.image, let2.image = let2.image, let1.image
                let1.key, let2.key = let2.key, let1.key
        self.letters.draw(self.screen)
        self.screen.blit(self.frame.frame_surface(), (x, 91))


        print(self.frame.rect)
        print(self.letters)

    def button_click(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.rect.collidepoint(x, y):
                    if button.key == "R":
                        self.move_right()
                    if button.key == "L":
                        self.move_left()
                    if button.key == "O":
                        self.swap()

    def button_light(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.rect.collidepoint(x, y):
                    button.light_on()
                else:
                    button.light_off()

    def main_loop(self):
        self.draw_board()
        while True:
            self.event_loop()

    # event loop to implements events
    def event_loop(self):
        for event in pygame.event.get():
            print(event)
            self.button_click(event)
            self.button_light(event)
            self.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    # starts the game
    def run(self):
        self.main_loop()


g = Game()

g.run()