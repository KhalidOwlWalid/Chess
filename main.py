import pygame
from src import gameState, board


def readable_board(board):
    for row in board:
        print(row)

# CONSTANTS
ROWS = 8
COLUMNS = 8
HEIGHT = 300
WIDTH = 300
SQ_SIZE = WIDTH // ROWS

# debug constant
debug = 0
debug_time = 30

# Screen constants
WIDTH = 300
HEIGHT = 300
SIZE = (WIDTH, HEIGHT)

# Color
BLACK = (0,0,0)
WHITE = (255,255,255)

# Game State 
num_of_turns = 0
FPS = 30
fpsclock = pygame.time.Clock()
colorTurn = 0

#--------------------------------------------------------Game starts here--------------------------------------------------------#
pygame.init()

# Set the size of the screen to be 800,800
screen = pygame.display.set_mode(SIZE)

running = True

gs = gameState.GameState()
b = board.Board(gs.board)

b.load_images()

userClicks = []


while running:
    
    
    for event in pygame.event.get():

        #if debug % debug_time == 0:
            #print("Under event : ", white_move)

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            location = pygame.mouse.get_pos()
            x,y = location

            # Get the row and column of which box is pressed
            row = y // SQ_SIZE
            column = x // SQ_SIZE
            location = (column, row)

            squareSelected = location

            userClicks.append(squareSelected)

            #pieceColumn, pieceRow = userClicks[0]
            #print(gs.board[pieceRow][pieceColumn])

            if len(userClicks) == 2:

                if colorTurn % 2 == 0:
                    m = gameState.Move(userClicks[0],userClicks[1], gs.board, True)
                    colorTurn += 1
                else:
                    m = gameState.Move(userClicks[0],userClicks[1], gs.board, False)
                    colorTurn += 1

                readable_board(gs.board)

                userClicks = [] # Refresh the users  click after making a move
                
                
    b.draw_game_state(screen)
    
    pygame.display.flip()
    # Update the display 
    pygame.display.update()
    fpsclock.tick(FPS)
    
    debug += 1

pygame.quit()

