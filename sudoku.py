from sudoku_generator import SudokuGenerator
from cell import Cell
from board import Board
import pygame
from pygame.locals import *




#source: https://www.geeksforgeeks.org/introduction-to-pygame/
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()

        # Define the dimension of the surface
        self.surf = pygame.Surface((80, 35))

        # Define the color of the surface
        self.surf.fill((255, 128, 0))
        self.rect = self.surf.get_rect()

        """
        square1 = Square()
        square2 = Square()
        square3 = Square()

        # Define where the squares will appear on the screen
        # Use blit to draw them on the screen surface
        screen.blit(square1.surf, (90, 400))
        screen.blit(square2.surf, (210, 400))
        screen.blit(square3.surf, (330, 400))
        """

grey = (224, 224, 224)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 128, 0)
lightblue = (153, 204, 255)

# Define the dimensions of screen object
screen = pygame.display.set_mode((500, 600))


def home_screen():
    font = pygame.font.SysFont('arial', 55, True, False)
    font2 = pygame.font.SysFont('arial', 45, False, False)
    font3 = pygame.font.SysFont('calibri', 35, True, False)

    text = font.render('Welcome to Sudoku', True, black, grey)
    welcome = text.get_rect()
    welcome.center = (500 // 2, 100)

    text2 = font2.render('Select Game Mode:', True, lightblue, grey)
    mode = text.get_rect()
    mode.center = (310, 300)

    text3 = font3.render(' EASY ', True, white, orange)
    easy = text3.get_rect()
    easy.center = (100, 400)

    text4 = font3.render(' MEDIUM ', True, white, orange)
    medium = text4.get_rect()
    medium.center = (250, 400)

    text5 = font3.render(' HARD ', True, white, orange)
    hard = text5.get_rect()
    hard.center = (400, 400)

    screen.fill(grey)
    screen.blit(text, welcome)
    screen.blit(text2, mode)
    screen.blit(text3, easy)
    screen.blit(text4, medium)
    screen.blit(text5, hard)




def main():

    gameOn = True

    while gameOn:
        pygame.init()

        # set the pygame window name
        pygame.display.set_caption('Group_13_Sudoku')

        home_screen()

        #THIS IS REQUIRED TO DISPLAY PYGAME GRAPHICS
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()










if __name__ == '__main__':
    main()
