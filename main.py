from board import Board, SQ_SIZE
import pygame
from gameState import GameState, Move

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
b.draw_game_state(screen)

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
                m = Move(userClicks, gs.board)
                m.move_pawn()
                


    #b.draw_board(screen)
    #b.draw_chess_pieces(screen)
    

    # get mouse click
    # check mouse location
    # divide it to get the rows and columns of the position of cursor
    # check selected square
    # create a list that keep tracks of users clicks

    # Update the display S
    pygame.display.update()

pygame.quit()

