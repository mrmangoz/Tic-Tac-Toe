import pygame
import numpy
from symbols import Symbols
from symbol import Symbol
pygame.init()

BLUE = 0, 0, 255
RED = 255, 0, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0
end = False
player = "X"
grid = numpy.zeros((9), dtype=int)  # creates the grid of 0s
grid = grid.reshape(3, 3)  # reshapes it to a 2d grid

#  50,50
#  251,251


def get_pos(m):
    if 50 < m < 117:
        g = 0
    elif 117 < m < 184:
        g = 1
    elif 184 < m < 251:
        g = 2
    return(g)


def draw_lines():
    for i in range(2):
        coord = 67*(i+1)
        pygame.draw.rect(background, BLACK, [50, 50 + coord, 201, 1])
        pygame.draw.rect(background, BLACK, [50 + coord, 50, 1, 201])


def coords(n):
    if 50 < n < 117:
        return(1)
    elif 117 < mx < 184:
        return(2)
    elif 184 < mx < 251:
        return(3)


def draw_symbol(symbol):
    offx = 67*symbol.pos[0]
    offy = 67*symbol.pos[1]
    if symbol.type == "X":
        pygame.draw.rect(background, BLUE, [50 + offx, 50 + offy, 67, 67])
        screen.blit(background, (0, 0))
        pygame.display.flip()
    elif symbol.type == "O":
        pygame.draw.rect(background, RED, [50 + offx, 50 + offy, 67, 67])
        screen.blit(background, (0, 0))
        pygame.display.flip()


screen = pygame.display.set_mode((300, 300))  # creates the screen
background = pygame.Surface((300, 300))  # creates the background image
background = background.convert()
board = pygame.Surface((300, 300))
pygame.draw.rect(background, WHITE, [50, 50, 201, 201])
draw_lines()
screen.blit(background, (0, 0))  # blits background onto screen
pygame.display.flip()  # updates display
symbols = Symbols()
symbol = Symbol()


while not end:
    for event in pygame.event.get():  # deteremines which key is pressed
        if event.type == pygame.QUIT:  # if you click the quit :(
            end = True  # breaks the while loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mx = mouse_pos[0]
            my = mouse_pos[1]
            if 50 <= mx <= 251 and 50 <= my <= 251:
                grid_pos = (get_pos(mx), get_pos(my))
                symbol.add(grid_pos)
                draw_symbol(symbol)
                symbols.add(symbol)
                symbol.switch()
                print("line check", symbols.line_check(symbol))
                print(grid_pos)
