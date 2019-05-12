import pygame
from game1v2.Resize import Resize
from game1v2.Letters import Letters
from game1v2.Letter import Letter
from game1v2.Frame import Frame
from game1v2.Buttons import Buttons
from game1v2.Button import Button
from game1v2.Text import Text

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
        self.unsorted_key = random.sample(self.letters_key, 10)
        self.steps = self.bubble_sort([key for key in self.unsorted_key])
        print(len(self.steps))
        self.actual_step = 0

    def swap_validator(self, let1, let2):
        if self.steps[self.actual_step] == (let1.key, let2.key):
            self.actual_step += 1
            if self.actual_step == len(self.steps):
                return "wygrałeś!"
            print(self.steps[self.actual_step])
        else:
            return "przegrałeś"

    def bubble_sort(self, arr):
        n = len(arr)
        steps = []
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    steps.append((arr[j], arr[j + 1]))
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return steps

    def draw_board(self):
        print(self.unsorted_key)

        for num, key in enumerate(self.unsorted_key):
            self.letters.add(Letter(key, 269 + (num * 50)))
        for key in self.buttons_positions.keys():
            self.buttons.add(Button(key, self.buttons_positions[key], self.buttons_light_position[key]))
        self.update()

    def update(self):
        self.screen.blit(self.background_image, (0, 0))
        self.letters.draw(self.screen)
        self.buttons.draw(self.screen)
        self.screen.blit(self.frame.frame_surface(), (self.frame.rect[0], self.frame.rect[1]))

    def move_right(self):
        x, y = self.frame.rect[0], self.frame.rect[1]
        if x < 669:
            x += 50
        self.screen.blit(self.frame.frame_surface(), (x, y))
        self.frame.rect[0] = x

    def move_left(self):
        x, y = self.frame.rect[0], self.frame.rect[1]
        if x > 269:
            x -= 50
        self.screen.blit(self.frame.frame_surface(), (x, y))
        self.frame.rect[0] = x

    def swap(self):
        x, y = self.frame.rect[0], self.frame.rect[1]
        let_iter = iter(self.letters.sprites())
        for letter in let_iter:
            if letter.position[0] == x:
                let1 = letter
                let2 = next(let_iter)
                print(self.swap_validator(let1, let2))
                let1.image, let2.image = let2.image, let1.image
                let1.key, let2.key = let2.key, let1.key
        self.letters.draw(self.screen)
        self.screen.blit(self.frame.frame_surface(), (x, 91))


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
            self.button_click(event)
            self.button_light(event)
            self.update()
            pygame.display.flip()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    # starts the game
    def run(self):
        self.main_loop()


g = Game()

g.run()