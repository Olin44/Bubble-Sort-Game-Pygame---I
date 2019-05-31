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
        self.SCALE = 2
        self.fps = 30
        self.clock = pygame.time.Clock()
        mb_position = (280, 400)
        pygame.init()

        self.background_image = pygame.image.load("graphics/start.png")
        self.background_image, self.size = Resize(self.background_image, self.SCALE).resize()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Bubble Sort Game")

        self.frame = ""
        self.letters = Letters()
        self.buttons = Buttons()
        self.frames = pygame.sprite.Group()
        self.menu_button = Button("S", mb_position, mb_position, self.SCALE)
        self.buttons.add(self.menu_button)
        self.letters_key = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'N', 'O', 'P', 'R', 'S', 'X', 'Z')
        self.buttons_positions = {'L': (self.size[0] / 3.42, self.size[1] / 3.27),
                                  'O': (self.size[0] / 1.41, self.size[1] / 3.27),
                                  'R': (self.size[0] / 2.56, self.size[1] / 3.27)}
        self.buttons_light_position = {'L': (self.size[0] / 3.55, self.size[1] / 3.48),
                                       'O': (self.size[0] / 1.44, self.size[1] / 3.48),
                                       'R': (self.size[0] / 2.59, self.size[1] / 3.48)}
        self.unsorted_key = random.sample(self.letters_key, 10)
        self.steps = self.bubble_sort([key for key in self.unsorted_key])
        self.actual_step = 0
        self.end_game = "start"
        print(len(self.steps))
        print(self.steps[self.actual_step])

    def swap_validator(self, let1, let2):
        try:
            if self.steps[self.actual_step] == (let1.key, let2.key):
                self.actual_step += 1
                if self.actual_step == len(self.steps):
                    self.end_game = 1
                print(self.steps[self.actual_step])
            else:
                self.end_game = "fail"
        except IndexError:
                self.end_game = "win"



    def bubble_sort(self, arr):
        n = len(arr)
        steps = []
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    steps.append((arr[j], arr[j + 1]))
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return steps

    def update(self):
        self.screen.blit(self.background_image, (0, 0))
        self.buttons.draw(self.screen)
        self.letters.draw(self.screen)
        self.frames.draw(self.screen)

    def draw_board(self):
        self.frame = Frame(self.size[0] / 3.56, self.size[1] / 5.93, self.SCALE)
        self.frames.add(self.frame)
        for num, key in enumerate(self.unsorted_key):
            self.letters.add(Letter(key, 269 + (num * 50), self.SCALE))
        for key in self.buttons_positions.keys():
            self.buttons.add(Button(key, self.buttons_positions[key], self.buttons_light_position[key], self.SCALE))
        self.update()

    def move_right(self):
        x, y = self.frame.get_coordinate_xy()
        if x < self.size[0] / 1.5:
            x += self.size[0] / 19.2
        self.screen.blit(self.frame.frame_surface(), (x, y))
        self.frame.set_position_x(x)

    def move_left(self):
        x, y = self.frame.get_coordinate_xy()
        if x > self.size[0] / 3.5:
            x -= self.size[0] / 19.2
        self.screen.blit(self.frame.frame_surface(), (x, y))
        self.frame.set_position_x(x)

    def swap(self):
        x, y = self.frame.get_coordinate_xy()
        let_iter = iter(self.letters.sprites())
        for letter in let_iter:
            if letter.get_position_x() == x:
                let1 = letter
                let2 = next(let_iter)
                self.swap_validator(let1, let2)
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
                    if button.key == "S":
                        self.end_game = "play"
                    if button.key == "F":
                        self.end_game = "start"

    def button_light(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.rect.collidepoint(x, y):
                    button.light_on()
                else:
                    button.light_off()

    #main game loop
    def main_loop(self):
        while True:
            self.clock.tick(self.fps)
            while self.end_game == "start":
                self.screen.blit(self.background_image, (0, 0))
                self.event_loop()
            self.draw_board()
            while self.end_game == "play":
                self.buttons.remove(self.menu_button)
                self.background_image = Resize(pygame.image.load("graphics/chest.png")).img
                self.event_loop()
            while self.end_game == "fail":
                self.background_image = Resize(pygame.image.load("graphics/fail.png")).img
                self.menu_button.key = "F"
                self.buttons = Buttons()
                self.letters = Letters()
                self.frames = pygame.sprite.Group()
                self.buttons.add(self.menu_button)
                self.screen.blit(self.background_image, (0, 0))
                self.event_loop()
            while self.end_game == "win":
                self.background_image = Resize(pygame.image.load("graphics/end.png")).img
                self.menu_button.key = "S"
                self.buttons = Buttons()
                self.letters = Letters()
                self.frames = pygame.sprite.Group()
                self.buttons.add(self.menu_button)
                self.screen.blit(self.background_image, (0, 0))
                self.event_loop()
            if self.end_game == "start":
                self.__init__()


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