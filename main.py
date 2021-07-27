from board import Board
import pygame
from gameState import GameState

WIDTH = 800
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)

# Color
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

# Set the size of the screen to be 800,800
screen = pygame.display.set_mode(SIZE)

running = True

b = Board()
b.load_images()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    b.draw_board(screen)
    #b.draw_chess_pieces()

    # Update the display 
    pygame.display.update()

pygame.quit()

