from board import Board, SQ_SIZE
import pygame
from gameState import GameState, Move


def readable_board(board):

    for row in board:
        print(row)


WIDTH = 300
HEIGHT = 300
SIZE = (WIDTH, HEIGHT)

# Color
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

# Set the size of the screen to be 800,800
screen = pygame.display.set_mode(SIZE)

running = True

gs = GameState()
b = Board(gs.board)

b.load_images()

userClicks = []


while running:
    
    
    for event in pygame.event.get():

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
            print(userClicks)

            if len(userClicks) == 2:
                m = Move(userClicks[0],userClicks[1], gs.board)
                m.move_pawn()
                readable_board(gs.board)
                userClicks = [] # Refresh the users  click after making a move
                
    
    b.draw_game_state(screen)
    
    pygame.display.flip()
    # Update the display S
    pygame.display.update()

pygame.quit()

