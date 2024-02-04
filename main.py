import pygame
import math

pygame.init()

SCREEN_SIZE = 500

# Set up the drawing window
SCREEN = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
pygame.display.set_caption('Checkers')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

def draw_board():
    SCREEN.fill((245, 231, 198))
    for x in range(8):
        for y in range(8):
            if (x + y) % 2 == 0:
                pygame.draw.rect(SCREEN, (46, 42, 38), (x*((SCREEN_SIZE/8)), y*(SCREEN_SIZE/8), SCREEN_SIZE/8, SCREEN_SIZE/8))

def draw_checker(x, y, color=1):
    x = x*((SCREEN_SIZE/8)) + (SCREEN_SIZE/8)/2
    y = y*(SCREEN_SIZE/8) + (SCREEN_SIZE/8)/2
    color_1 = (212, 183, 131) if color == 0 else (84, 82, 80)
    color_2 = (230, 211, 177) if color == 0 else (102, 100, 97)
    pygame.draw.circle(SCREEN, color_1, (x, y), SCREEN_SIZE/16-3)
    pygame.draw.circle(SCREEN, color_2, (x, y), SCREEN_SIZE/16-9)
    pygame.draw.circle(SCREEN, color_1, (x, y), SCREEN_SIZE/16-15)

def draw_checkers(checker_board):
    for x in range(4):
        for y in range(8):
            if checker_board[y][x] != 0:
                draw_checker((x*2)+(y%2), y, checker_board[y][x]-1)

checker_board = [[2, 2, 2, 2],
                 [2, 2, 2, 2],
                 [2, 2, 2, 2],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1]]
    
# Run until the user asks to quit
running = True
disp_update = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = (math.floor(p*8/SCREEN_SIZE) for p in pos)
            print(x, y)

    draw_board()
    draw_checkers(checker_board)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()