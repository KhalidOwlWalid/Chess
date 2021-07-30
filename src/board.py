import pygame
from src import gameState

# CONSTANTS
ROWS = 8
COLUMNS = 8
HEIGHT = 300
WIDTH = 300
SQ_SIZE = WIDTH // ROWS

# COLOR
WHITE = (255,255,255)
BLACK = (0,0,0)

gs = gameState.GameState()

class Board:

    def __init__(self, board):
        self.board = board

    # This function will help us load all the sprites from our folder
    def load_images(self):
        
        chess_pieces = {}

        pieces = ["bR","bKN","bB","bQ","bK","bP","wR","wKN","wB","wQ","wK", "wP"]

        for piece in pieces:
            chess_pieces[piece] = pygame.transform.scale(pygame.image.load("Assets/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

        return chess_pieces

    
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
                

    def draw_chess_pieces(self, screen):
        
        chess_pieces = self.load_images()

        for column in range(COLUMNS):
            for row in range(ROWS):
                piece = self.board[column][row]
                if piece != "--":
                    screen.blit(chess_pieces[piece], pygame.Rect(row*SQ_SIZE, column * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def draw_game_state(self, screen):
        self.draw_board(screen)
        self.draw_chess_pieces(screen)
