from sudoku_generator import SudokuGenerator
from cell import Cell
from board import Board
import pygame
from pygame.locals import *
from os import system

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


def button(screen, position, text):
    font = pygame.font.SysFont("calibri", 40)
    text_render = font.render(text, 1, (255, 255, 255))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (255, 128, 0), (x, y, w , h))
    return screen.blit(text_render, (x, y))

def button_small(screen, position, text):
    font = pygame.font.SysFont("calibri", 30)
    text_render = font.render(text, 1, (255, 255, 255))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (255, 128, 0), (x, y, w , h))
    return screen.blit(text_render, (x, y))



def main():

    while True:
        #set the pygame window name
        pygame.display.set_caption('Group_13_Sudoku')
        home_screen()

        easy = button(screen, (50, 400), "EASY")
        medium = button(screen, (170, 400), "MEDIUM")
        hard = button(screen, (350, 400), "HARD")

        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                    if key_to_start:
                        start()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy.collidepoint(pygame.mouse.get_pos()):
                        screen.fill(grey)
                        reset = button_small(screen, (90, 550), "RESET")
                        restart = button_small(screen, (210, 550), "RESTART")
                        exit_ = button_small(screen, (360, 550), "EXIT")
                    elif medium.collidepoint(pygame.mouse.get_pos()):
                        screen.fill(grey)
                        reset = button_small(screen, (90, 550), "RESET")
                        restart = button_small(screen, (210, 550), "RESTART")
                        exit_ = button_small(screen, (360, 550), "EXIT")
                    elif hard.collidepoint(pygame.mouse.get_pos()):
                        screen.fill(grey)
                        reset = button_small(screen, (90, 550), "RESET")
                        restart = button_small(screen, (210, 550), "RESTART")
                        exit_ = button_small(screen, (360, 550), "EXIT")

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if exit_.collidepoint(pygame.mouse.get_pos()):
                            pygame.quit()
            pygame.display.update()
        pygame.quit()











if __name__ == '__main__':
    main()
