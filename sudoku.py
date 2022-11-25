from sudoku_generator import SudokuGenerator
from cell import Cell
from board import Board
import pygame
from pygame.locals import *

#source: https://www.geeksforgeeks.org/introduction-to-pygame/
#source: https://www.geeksforgeeks.org/how-to-use-multiple-screens-on-pygame/
#source: https://pythonprogramming.altervista.org/buttons-in-pygame/




#colors
grey = (224, 224, 224)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 128, 0)
lightblue = (153, 204, 255)

pygame.init()
screen = pygame.display.set_mode((500, 600))
font = pygame.font.SysFont("arial", 40)
clock = pygame.time.Clock()


def home_screen():
    font = pygame.font.SysFont('franklingothic', 60, False, False)
    font2 = pygame.font.SysFont('franklingothic', 45, False, False)

    text = font.render('Welcome to Sudoku', True, black, grey)
    welcome = text.get_rect()
    welcome.center = (500 // 2, 100)

    text2 = font2.render('Select Game Mode:', True, black, grey)
    mode = text.get_rect()
    mode.center = (310, 300)

    screen.fill(grey)
    screen.blit(text, welcome)
    screen.blit(text2, mode)


class Button:
    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("calibri", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, 1, pygame.Color(white))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(button1.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, 'lightblue')





button1 = Button("EASY", (100, 400), 30, orange, "START EASY MODE")
button2 = Button("MEDIUM", (200, 400), 30, orange, "START MEDIUM MODE")
button3 = Button("HARD", (300, 400), 30, orange, "START HARD MODE")


def main():

    while True:
        #set the pygame window name
        pygame.display.set_caption('Group_13_Sudoku')
        home_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event)

        button1.show()
        clock.tick(30)
        pygame.display.update()

        pygame.display.flip()









if __name__ == '__main__':
    main()
