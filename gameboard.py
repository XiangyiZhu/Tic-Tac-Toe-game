class BoardClass:
    """ Operate the game board.

    The class contains, updates, and shows all the information of
    the two players and the board.

    Attributes:
        player1: user name of player 1.
        player2: user name of player 2.
        lastplayer: user name of the last player to have a turn(str).
        wins: number of wins(int).
        ties: number of ties(int).
        losses: number of losses(int).
        board: the game board with players' move.
        games: the total number of games played.
        move: all the moves made by two players

    """
    def __init__(self,  player1or2: int = 0, player1: str = "", player2: str = "", lastplayer: str = "", wins: int= 0, ties: int = 0, losses: int = 0, board: list = [], games: int = 0, move: list = []) -> None:
        """
        Set up the initializations.

        Args:
            player1: user name of player 1.
            player2: user name of player 2.
            lastplayer: User name of the last player to have a turn.    
            wins: Number of wins.
            ties: Number of ties.
            losses:Number of losses.
            board: the game board with players' move.
            games: Number of total games.
            move: each move.

        """
        self.player1or2 = player1or2
        self.player1 = player1
        self.player2 = player2
        self.lastplayer = lastplayer
        self.wins = wins
        self.ties = ties
        self.losses = losses
        self.board = [[" "]*3, [" "]*3, [" "]*3]
        self.games = games
        self.move = []


    def updateGamesPlayed(self):
        """
        Keeps track how many games have started.

        """
        self.games += 1


    def resetGameBoard(self):
        """
        Resets the game board and clears all the moves.

        """
        self.board = [[" "]*3, [" "]*3, [" "]*3]
        self.move = []
        


    def updateGameBoard(self, currentplayer, move):
        """
        Updates the game board.

        Args:
            currentplayer: the player who is making the move.
            move: the move maded by the player.

        """  
        move = str(move)
        row = int(move[0])-1
        col = int(move[1])-1
        if self.player1or2 == 1:
            if currentplayer == self.player2:
                self.board[row][col] = "O"
            else:
                self.board[row][col] = "X"
        elif self.player1or2 == 2:
            if currentplayer == self.player2:
                self.board[row][col] = "X"
            else:
                self.board[row][col] = "O"
        self.move.append(move)
        self.lastplayer = currentplayer
        

    def isWinner(self):
        """
        Checks if the latest move resulted in a win
        and updates the wins and losses count.

        Returns:
            True: someone wins the game.
            False: no one wins the game yet.

        """
        if self.move:
            row = int(self.move[-1][0])-1
            col = int(self.move[-1][1])-1
            XorO = self.board[row][col]
            boardrow = all(element == XorO for element in self.board[row])
            boardcol = all(element == XorO for element in [self.board[0][col],self.board[1][col],self.board[2][col]])
            boardcross1 = all(element == XorO for element in [self.board[0][0],self.board[1][1],self.board[2][2]])
            boardcross2 = all(element == XorO for element in [self.board[0][2],self.board[1][1],self.board[2][0]])
            if boardrow or boardcol or boardcross1 or boardcross2:
                if (self.player1or2 == 1 and XorO == "X") or (self.player1or2 == 2 and XorO == "O"):
                    self.wins += 1
                else:
                    self.losses += 1
                self.updateGamesPlayed()
                return True
            else:
                return False
        else:
            return False

 

    def boardIsFull(self):
        """
        Checks if the board is full and updates the ties count.

        Returns:
            True: if the board is full.
            False: the board is not full.
        """
        if all(" " not in element for element in self.board):
            self.updateGamesPlayed()
            self.ties += 1
            return True
        else:
            return False


    def computeStats(self):
        """
        Computes and return both players' user name, the user name of the last person to make a move,
        number of games, the number of wins, the number of losses, the number of ties.
        """
        
        return self.player1, self.player2, self.games, self.wins, self.losses, self.ties

     
    def displayStats(self):
        """
        Presents the current board state to players after each player makes a move.
        """
        aa,bb,cc,dd,ee,ff = self.computeStats()
        a = f"Final Statistics\nUser Name of Player1 = my name: {aa}\n"
        b = f"User Name of Player2: {bb}\n"
        c = f"The number of games: {cc}\n"
        d = f"The number of wins: {dd}\n"
        e = f"The number of losses: {ee}\n"
        f = f"The number of ties: {ff}\n"
        return a+b+c+d+e+f


    def gameover(self):
        """
        Checks whether the game is over: the game is over when there is a winner or the board if full.

        Returns:
            True: the game is over as the board is full or someone has winned the game.
            False: the game is not over.
        """
        if self.isWinner() == False and self.boardIsFull() == False:
            return False
        else:
            return True



        



        
    
