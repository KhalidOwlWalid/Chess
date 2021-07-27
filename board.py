import pygame
from gameState import GameState
# CONSTANTS
ROWS = 8
COLUMNS = 8
HEIGHT = 800
WIDTH = 800
SQ_SIZE = WIDTH // ROWS

# COLOR
WHITE = (255,255,255)
BLACK = (0,0,0)

gs = GameState()

class Board:

    def __init__(self):
        self.board = gs.board

    # This function will help us load all the sprites from our folder
    def load_images(self):
        for row in self.board:
            for i,column in enumerate(row):
                try:
                    pygame.image.load("Assets/" + column +  ".png")
                except:
                    pass
    
    # draw our chess board 
    def draw_board(self, screen):

        colors = [pygame.Color("white"), pygame.Color("gray")]
        for row in range(ROWS):
            for column in range(COLUMNS):
                # Remember that the box will always start with white at the top right corner of the chess board
                # Index helps us change color from white to gray separately
                index = (row+column) % 2
                color = colors[index]
                pygame.draw.rect(screen, color, (column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                

    def draw_chess_pieces(self):
        pass