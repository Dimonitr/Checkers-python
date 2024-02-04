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

def check_tile(selected, checker_board):
    x, y = selected
    if (x-(y%2))/2 < 0 or (x-(y%2))/2 != int((x-(y%2))/2):
        return None
    return checker_board[y][int((x-(y%2))/2)]
    

def get_legal_moves(selected, checker_board):
    x, y = selected
    legal_moves = []
    if  y-1 >= 0 and x-1 >= 0 and check_tile((x-1,y-1), checker_board) == 0:
        legal_moves.append((x-1, y-1))
    if  y+1 < 8 and x-1 >= 0 and check_tile((x-1,y+1), checker_board) == 0:
        legal_moves.append((x-1, y+1))
    if  y-1 >= 0 and x+1 < 8 and check_tile((x+1,y-1), checker_board) == 0:
        legal_moves.append((x+1, y-1))
    if  y+1 < 8 and x+1 < 8 and check_tile((x+1,y+1), checker_board) == 0:
        legal_moves.append((x+1, y+1))
    return legal_moves

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
player = 1
state = "select" # select, move
selected = (-1, -1)
legal_moves = []

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = (math.floor(p*8/SCREEN_SIZE) for p in pos)
            match state:
                case "select":
                    if check_tile((x, y), checker_board) == player:
                        state = "move"
                        selected = (x, y)
                        legal_moves = get_legal_moves(selected, checker_board)
                        print(legal_moves)
                case "move":
                    if (x, y) in legal_moves:
                        checker_board[y][int((x-(y%2))/2)] = checker_board[selected[1]][int((selected[0]-(selected[1]%2))/2)]
                        checker_board[selected[1]][int((selected[0]-(selected[1]%2))/2)] = 0
                        player = 1 if player == 2 else 2
                        disp_update = True
                        state = "select"
                        selected = (-1, -1)
                        legal_moves = []
                    else:
                        state = "select"
                        selected = (-1, -1)
                        legal_moves = []

    draw_board()
    draw_checkers(checker_board)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()