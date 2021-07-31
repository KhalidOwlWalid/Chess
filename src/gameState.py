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
    def __init__(self,startMove,endMove, board, player_turn):
        # Include the  GameState Class
        self.gameState = GameState()

        # Get all the coordinates and sort it out
        self.startMove = startMove
        self.endMove = endMove
        self.startColPosition, self.startRowPosition = startMove
        self.endColPosition, self.endRowPosition = endMove
        self.board = board
        self.white_move = player_turn

        # Which piece is the user grabbing and where is he going to move?
        self.piece = board[self.startRowPosition][self.startColPosition]
        self.userMove = board[self.endRowPosition][self.endColPosition]

        # Check chess piece type
        self.check_piece()

    def check_piece(self):

        if self.piece == "wP" or self.piece == "bP":
            self.move_pawn()
  
        elif self.piece == "wR" or self.piece == "bR":
            print("Rook here")
            self.move_rook()

        elif self.piece == "wB" or self.piece == "bB":
            print("Bishop here")
            self.move_bishop()

        elif self.piece == "wKN" or self.piece == "bKN":
            print("Knight here")
            self.move_knight()

        elif self.piece == "wK" or self.piece == "bK":
            print("King here")
            self.move_king()

        elif self.piece == "wQ" or self.piece == "bQ":
            print("My queen alia is here")
            self.move_queen()

    def moveCalculator(self):

        startCol, startRow = self.startMove
        endCol, endRow = self.endMove

        calculateCol = endCol - startCol
        calculateRow = endRow - startRow

        return (calculateCol, calculateRow)

    def take_or_swap(self):

        self.board[self.startRowPosition][self.startColPosition] = "--"
        self.board[self.endRowPosition][self.endColPosition] = self.piece

    def move_pawn(self):

        wPStartPosition = [(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
        bPStartPosition = [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

        # Pawn movement allowed
        wPAllowedMovement = [(0,-1), (0,-2)]
        bPAllowedMovement = [(0,1), (0,2)]

        # Get the piece at the start position to check chess piece type
        pawnPosition = self.board[self.startRowPosition][self.startColPosition]

        userMove = self.moveCalculator()

        if self.white_move == True and pawnPosition == "wP":

            if userMove in wPAllowedMovement:

                if self.startMove in wPStartPosition:
                    self.take_or_swap()
                    print("Black Turn")

                    return False

                else:
                    self.take_or_swap()
                    print("Black Turn")

                    return False

            # If the player attempt to jump more than 2 boxes or move diagonally, it is not allowed hence telling them it is an invalid move
            else:
                print("Invalid move, please try again")
                print("White Turn")

                return True


        if self.white_move == False and pawnPosition == "bP":
            
            if userMove in bPAllowedMovement:

                if self.startMove in bPStartPosition:
                    self.take_or_swap()
                    print("White turn")

                    return True

                else:
                    self.take_or_swap()
                    print("White turn")

                    return True

            
            else:
                print("Invalid move, please try again")

                return False

    def move_rook(self):  

        print(self.piece)

    def move_knight(self):
        print(self.piece)

    def move_bishop(self):
        print(self.piece)

    def move_queen(self):
        print(self.piece)

    def move_king(self):
        print(self.piece)


            


