#------------------#
# Module Importing # (M.T)
#------------------#
import numpy as np
import pygame
import sys
import math
#------------------#
# Global Variables #
#------------------#
# Set initial (RGB 8 bit) color values (M.T) 
BLACK = (0,0,0) # Board Color (M.T)
WHITE = (255,255,255) # Background Color (M.T)
RED = (255,0,0) # Player 1 Color (M.T)
CYAN = (0,255,255) # Player 2 Color (M.T)
 
# Set initial size of playing board (M.T) 
ROW_COUNT = 6
COLUMN_COUNT = 7
 
################
# SUB-PROGRAMS # (M.T)
################

# Function to create the playing board (2D np.array) (M.T)
# Call from MAIN (M.T)
# Returns board (np.array) (M.T)
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board
  
# Function to drop piece (M.T)
# Call from MAIN (M.T)
# Requires 'board (np.array)'; 'row (int)'; 'col (int)'; 'piece (int)' (M.T)  
# 'piece' will be 1 or 2 (Which Player's Turn) (M.T)
# 'row'; 'col' depends on user mouse position (M.T)
def drop_piece(board, row, col, piece):
    board[row][col] = piece
 
# Function to test for valid drop position (M.T)  
# Call from MAIN (M.T) 
# Requires 'board (np.array)'; 'col (int)' (M.T) 
# Returns 'board (np.array)' (M.T) 
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0 # Return valid location (M.T) 
 
# Function to find next open row (M.T) 
# Call from MAIN  (M.T) 
# Requires 'board (np.array)'; 'col (int)' (M.T) 
# Returns 'None' or 'r' (Next valid Row) (M.T) 
def get_next_open_row(board, col):
    for r in range(ROW_COUNT): # Run through each row (Starting from top) (M.T) 
        if board[r][col] == 0: # If this row has value 0, this row is open and allows a piece to fill (M.T) 
            return r # Return the Row (M.T)
     
# Function to print the game board (ASCII array) (M.T) 
# Call from MAIN  (M.T) 
# Requires 'board (np.array)' (M.T)  
def print_board(board):
    print(np.flip(board, 0)) # Print the game board (ASCII array) (M.T) 
 
# Function to test for winning move (M.T)
# Call from MAIN  (M.T)
# Requires 'board (np.array)'; 'piece (int)' (M.T)
# Returns 'None' or True (M.T)
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece: # Has the player connected 4 in a row (horizontal) (M.T)
                return True
 
    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece: # Has the player connected 4 in a row (vertically) (M.T)
                return True
 
    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece: # Has the player connected 4 in a row (+diaganol) (M.T)
                return True
 
    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece: # Has the player connected 4 in a row (-diaganol) (M.T)
                return True
        
# Function to draw the game board (GUI-pygame) (M.T)
# Call from MAIN  (M.T)
# Requires 'board (np.array)' (M.T)  
def draw_board(board):
    for c in range(COLUMN_COUNT): # Print the background and Black Play Space (M.T)  
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
     
    for c in range(COLUMN_COUNT): # Print the game pieces (M.T)  
        for r in range(ROW_COUNT):      
            if board[r][c] == 1: # Check if value has player 1's piece (M.T)  
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: # Check if value has player 2's piece  (M.T)  
                pygame.draw.circle(screen, CYAN, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update() # Refresh the GUI buffer to print new objects (M.T)  
 
########
# MAIN # (M.T)
########
board = create_board() # Create the np.array for the game board (M.T)  
print_board(board) # Print the np.array (ASCII) (M.T)  
game_over = False  
turn = 0 # Player 1 starts their turn (M.T)  
TempColorChange = RED # Temp Variable for switching colors (M.T)
 
#initalize pygame
pygame.init()
 
# BELOW IS CODE TO SET UP GAME DIMENSIONS. THESE ARE ALL VARIBLE TO INSURE PROPER RATIOS OF ANY BOARD SIZE (M.T) 
 
#define our screen size 
SQUARESIZE = 100
 
#define width and height of board
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
 
size = (width, height) 
 
RADIUS = int(SQUARESIZE/2 - 5) # Set size of player pieces (M.T)   
 
screen = pygame.display.set_mode(size) # Set window screen size  (M.T)

#Calling function draw_board again
draw_board(board)
pygame.display.update() # Refresh the GUI buffer to print screen (M.T)
 
myfont = pygame.font.SysFont("monospace", 75) # Set game font (M.T)  
 
while not game_over: # Main game loop. Will end if user quits, or a player has won the game (M.T)
 
    for event in pygame.event.get(): # Main game event loop (M.T)
        if event.type == pygame.QUIT: # Has the user quit the game? (M.T)  
            sys.exit() # Exit the game
 
        # Print Player pieces while mouse moves on game screen (M.T)
        if event.type == pygame.MOUSEMOTION: # is the mouse moving? (M.T)
            pygame.draw.rect(screen, WHITE, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0: # If player 1's turn, draw the correct circle (M.T)
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else: # Then it is player 2's turn, draw the correct circle (M.T)
                pygame.draw.circle(screen, CYAN, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update() # Refresh the GUI buffer to print screen (Pieces moving with mouse) (M.T)
 
        if event.type == pygame.MOUSEBUTTONDOWN: # Has the player clicked the mouse, making a turn? (M.T) 
            pygame.draw.rect(screen, WHITE, (0,0, width, SQUARESIZE))
            #print(event.pos)
            # Ask for Player 1 Input
            if turn == 0: # Is it player 1's turn? (M.T)
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE)) # Find location at point of click (M.T)
 
                if is_valid_location(board, col): # User has clicked on a valid position (M.T)
                    row = get_next_open_row(board, col) # find the correct place to move piece (M.T)
                    drop_piece(board, row, col, 1) # Move the piece (M.T)
 
                    if winning_move(board, 1): # Has the player won the game? (M.T)
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True # Game is over - exit main game loop (M.T)
 
 
            # Ask for Player 2 Input
            else:               
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE)) # Find location at point of click (M.T)
 
                if is_valid_location(board, col): # User has clicked on a valid position (M.T)
                    row = get_next_open_row(board, col) # find the correct place to move piece (M.T)
                    drop_piece(board, row, col, 2) # Move the piece (M.T)
 
                    if winning_move(board, 2): # Has the player won the game? (M.T)
                        label = myfont.render("Player 2 wins!!", 1, CYAN)
                        screen.blit(label, (40,10))
                        game_over = True # Game is over - exit main game loop (M.T)
 
            print_board(board) # Print np.array (ASCII) (M.T)
            draw_board(board) # Draw the game board (pygame) (M.T)
 
            turn += 1 # Next players turn (M.T)
            turn = turn % 2 # Make the turn value 1 or 0 (M.T)
   
            # The swapping of colors (M.T)
            TempColorChange = RED
            RED = CYAN
            CYAN = TempColorChange
 
            if game_over: # gives enough time for players to view the 'wining game' message (M.T)
                pygame.time.wait(3000)
#Our completed GUI Connect Four(Colour Switch Edition)
