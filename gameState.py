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

    def __init__(self, userMove, board ):
        self.userMove = userMove
        self.board = board

    def move_pawn(self):

        print("I am working")
        column1, row1 = self.userMove[0]
        column2, row2 = self.userMove[1]
        
        if self.board[row1][column1] == "wP":
            self.board[row2][column2] = "--"
            self.board[row2][column2] = "wP"
    
