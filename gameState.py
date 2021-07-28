import pygame

class GameState:

    def __init__(self):
        
        self.board = [
        ["bR","bKN","bB","bQ","bK","bB","bKN","bR"],
        ["bP","bP","bP","bP","bP","bP","bP","bP"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["wP","wP","wP","wP","wP","wP","wP","wP"],
        ["wR","wKN","wB","wQ","wK","wB","wKN","wR"]]


class Move:

    # startMove and endMove takes an element of the userClicks where startMove = userClicks[0],  endMove = userClicks[1]
    def __init__(self, startMove,endMove, board ):
        self.startColPosition, self.StartRowPosition = startMove
        self.endColPosition, self.endRowPosition = endMove
        self.board = board

    def move_pawn(self):

        if self.board[self.StartRowPosition][self.startColPosition] == "wP":
            self.board[self.StartRowPosition][self.startColPosition] = "--"
            self.board[self.endRowPosition][self.endColPosition] = "wP"
            
        return self.board

