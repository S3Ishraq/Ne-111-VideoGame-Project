#Ethan Aumond (EA)



import numpy as np
import pygame
import sys
import math
 
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
CYAN = (0,255,255)
 
 #Number or rows/columns (EA)
ROW_COUNT = 6
COLUMN_COUNT = 7
 
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board
 
def drop_piece(board, row, col, piece):
    board[row][col] = piece
 
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0
 
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
 
def print_board(board):
    print(np.flip(board, 0))
 
def winning_move(board, piece):
    # Check horizontal locations for win (EA)
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece and board[r][c+4] == piece:
                return True
 
    # Check vertical locations for win (EA)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece and board[r+4][c] == piece:
                return True
 
    # Check positively sloped diaganols (EA)
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece and board[r+4][c+4] == piece:
                return True
 
    # Check negatively sloped diaganols (EA)
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece and board[r-4][c+4] == piece:
                return True
 
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
     
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, CYAN, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()
 
 
board = create_board()
print_board(board)
game_over = False
turn = 0
 
#initalize pygame
pygame.init()
 
#define our screen size
SQUARESIZE = 105
 
#define width and height of board
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
 
size = (width, height)
 
RADIUS = int(SQUARESIZE/2 - 5)
 
screen = pygame.display.set_mode(size)
#Calling function draw_board again
draw_board(board)
pygame.display.update()
 
myfont = pygame.font.SysFont("monospace", 75)
 
while not game_over:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, WHITE, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, CYAN, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, WHITE, (0,0, width, SQUARESIZE))
            #print(event.pos)
            # Ask for Player 1 Input (EA)
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
 
                    if winning_move(board, 1):
                        label = myfont.render("Game! P1 Wins", 1, RED)
                        screen.blit(label, (40,20))
                        game_over = True
 
 
            # # Ask for Player 2 Input (EA)
            else:               
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
 
                    if winning_move(board, 2):
                        label = myfont.render("Game! P2 Wins", 1, CYAN)
                        screen.blit(label, (40,20))
                        game_over = True
 
            print_board(board)
            draw_board(board)
 
            turn += 1
            turn = turn % 2
 
            if game_over:
                pygame.time.wait(3000)
