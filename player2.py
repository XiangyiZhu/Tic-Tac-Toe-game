import socket
from gameboard import BoardClass
import tkinter as tk
from tkinter import ttk

class UserInterface2():
    """
    Create the a Tic Tac Toe game where we use scokets to pass the moves between players and use tkinket to set up the canvas.

    """
    
    def __init__(self):
        """
        Set up the all the labels and buttons of the game board.
        """
        self.canvasSetup()
        self.initTKVvariables()
        self.createAddressEntry()
        self.createPortEntry()
        self.createConnectResultLabel()
        self.createConnectButton()
        self.receiveName1Lable()
        self.createUserNameEntry()
        self.UserNameLable()
        self.GameBoard()
        self.DisplayBoard()

        
    def initTKVvariables(self):
        """
        Define the initial varialbes.

        Variables:
            self.serverAddress: the server address entered by player2.
            self.serverPort: the port entered by player2.
            self.connection: the result of whether the connection is made successfully or not.
            self.username: the user name of player2 itself.
            self.user1name: the status of receiving the user name of player1.
            self.nameResult: the result of whether the user name entered by player2 is correct or not.
            self.result: the game progress, displaying who's turn it currently is or the game is over.
            self.game_over: True is game is over and False if not.
            self.statistics: the statistics of the game.
            self.decision: the decision made by player1 of whether to play again
        """
        self.serverAddress = tk.StringVar()
        self.serverPort = tk.IntVar()
        self.connection = tk.StringVar()
        self.receivename = tk.StringVar()
        self.username = tk.StringVar()
        self.user1name = tk.StringVar()
        self.nameResult = tk.StringVar()
        self.result = tk.StringVar()
        self.game_over = tk.BooleanVar(value=False)
        self.statistics = tk.StringVar(value = "Final Statistics")
        self.decision = tk.StringVar()
        
        
    def canvasSetup(self):
        """
        Initialize my tkinter canvas.
        """
        self.master = tk.Tk()
        self.master.title("Tic Tac Toe - Player2")
        self.master.geometry("820x600")
        self.master.configure(background = "white")
        self.master.resizable(1,1)

    
    def createAddressEntry(self):
        """
        Define a method that creates a serverAddress entry file.
        """
        laddress = tk.Label(self.master, text="Enter the address:")
        laddress.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.AddressEntry = tk.Entry(self.master, textvariable = self.serverAddress)
        self.AddressEntry.grid(row=0, column=1, padx=10, pady=5,sticky="w")


    def createPortEntry(self):
        """
        Define a method that creates a serverPort entry file.
        """
        laddress = tk.Label(self.master, text="Enter the port number:")
        laddress.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.PortEntry = tk.Entry(self.master, textvariable = self.serverPort)
        self.PortEntry.grid(row=1, column=1, padx=10, pady=5,sticky="w")   


    def createConnectButton(self):
        """
        Define a connect botton on the UI.
        """
        self.ConnectButton = ttk.Button(self.master,text= "Connect", command=self.connectToServer)
        self.ConnectButton.grid(row=2, column=0, padx=10, pady=5,sticky="w")
        

    def createConnectResultLabel(self):
        """
        Define a method that creates a label for my connection result.
        """
        result_label = tk.Label(self.master, textvariable=self.connection, width=25)
        result_label.grid(row=2, column=1, padx=10, pady=5,sticky="w")

        
    def receiveName1Lable(self):
        """
        Display the received the user name of player1.
        """
        namelable = tk.Label(self.master, textvariable=self.user1name, width=50)
        namelable.grid(row=3, columnspan=2, pady=5)

    
    def connectToServer(self):
        """
        Define a method that creates connection and receive the user name of player1.
        """
        self.connection.set("Waiting to be connected...")
        self.master.update()
        
        address = self.serverAddress.get()
        port = self.serverPort.get()

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((address, port))
        self.serverSocket.listen(1)
        self.clientSocket, self.clientAddress = self.serverSocket.accept()

        self.connection.set("Connected to a client!")
        self.master.update()

        self.user1name.set(f"Receiving another player's name...")
        self.master.update()
        
        global user_name_1
        user_name_1 = self.clientSocket.recv(2014).decode("ascii")
        self.user1name.set(f"Received the user name of another player: {user_name_1}")

        self.SubmitNameButton.config(state=tk.NORMAL)
        

    def createUserNameEntry(self):
        """
        Define a method that creates a UserName entry file and a button to submit the user name to player1.
        """
        lUserName = tk.Label(self.master, text="Enter the User Name:")
        lUserName.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.UserNameEntry = tk.Entry(self.master, textvariable = self.username)
        self.UserNameEntry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.SubmitNameButton = ttk.Button(self.master,text= "Submit the user name to another player.", command=self.UserNameSubmit, state=tk.DISABLED)
        self.SubmitNameButton.grid(row=5, column=0, padx=10, pady=5,sticky="w")

        
    def UserNameLable(self):
        """
        Display the result of whether the user name entered by player1 is correct or not.
        """
        result_label = tk.Label(self.master, textvariable=self.nameResult, width=25)
        result_label.grid(row=5, column=1, padx=10, pady=5,sticky="w")


    def UserNameSubmit(self):
        """
        If the user name is entered correctly, send the name to player1;
        else, clear the user name and prompt player2 to enter a new valid name.
        """
        
        global user_name_2, play2
        user_name_2 = self.username.get()

        if user_name_2.isalnum():
            self.clientSocket.send(user_name_2.encode())
            self.nameResult.set("Great! Sending it to another player...")
            self.master.update()

            self.SubmitNameButton.config(state=tk.DISABLED)
            play2 = BoardClass(2, user_name_2, user_name_1)

            self.firstmove()
            
        else:
            self.nameResult.set("Please enter a valid user name.")
            self.username.set("")


    def GameBoard(self):
        """
        Set up the game board canvas.
        """
        self.boardLabel = tk.Label(self.master, text="Tic Tac Toe - PLay Board", width=25)
        self.boardLabel.grid(row=6, column=0, padx=10, pady=5)
        
        gameboard = tk.Frame(self.master, width=250, height=250, bg='pink')
        
        self.buttons = [[None, None, None] for _ in range(3)]
        
        for i in range(0,3):
            for j in range(0,3):
                self.setupButton(gameboard,i,j)

        gameboard.grid(row=7, column=0,pady=5, padx=10)


    def setupButton(self,frame, x,y):
        """
        Set up the buttons on the game board.
        """
        button = tk.Button(frame, text="", command=lambda row=x, col=y: self.playboard(row, col), width=8, height=5, state=tk.DISABLED)
        button.grid(row=x, column=y)
        self.buttons[x][y] = button


    def firstmove(self):
        """
        Receive the first move of each game from player1.
        """

        self.result.set(f"It's {user_name_1}'s turn.")
        self.master.update()
            
        move1 = self.clientSocket.recv(2014).decode("ascii")
        play2.updateGameBoard(user_name_1, move1)

        button = self.buttons[int(move1[0])-1][int(move1[1])-1]
        if button["text"] == "":
            button.configure(text="X")
            self.result.set("It's your turn.")
            self.master.update()

        self.enableButtons()


    def playboard(self,row,col):
        """
        Define the button command, where player can click to make the move and the move will be sent to player1.

        Args:
            row: the row of the move made by player2.
            col: the col of the move made by player2.
        """
        if self.game_over.get() == True:
            return # do nothing if the game is over.
        
        button = self.buttons[row][col]
        if button["text"] == "":
            button.configure(text="O")
            self.disableButtons()
            self.master.update()

            self.result.set(f"It's {user_name_1}'s turn")
            self.master.update()

            move = f"{row+1}{col+1}"
            play2.updateGameBoard(user_name_2, move)

            self.movesubmit()


    def disableButtons(self):
        """
        Disable all buttons on the play board.
        """
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED) 


    def enableButtons(self):
        """
        Enable all buttons on the game board.
        """
        for row in self.buttons:
            for button in row:
                button.config(state=tk.NORMAL)


    def resetButtons(self):
        """
        Clear and reset the game board.
        """
        for row in self.buttons:
            for button in row:
                button.configure(text="", bg='white')
        play2.resetGameBoard()

        self.firstmove()


   
    def movesubmit(self):
        """
        Send the move and check the current status of the game:
        if game is over, end the game;
        else, if game is not over, continue the game by letting player1 make the move.
        """
        self.clientSocket.send(play2.move[-1].encode())
        
        if play2.gameover():
            self.result.set("Game Over!")
            self.master.update()
            self.gameover()

        else:
            move1 = self.clientSocket.recv(2014).decode("ascii")

            button = self.buttons[int(move1[0])-1][int(move1[1])-1]
            if button["text"] == "":
                button.configure(text="X")
                self.master.update()

            play2.updateGameBoard(user_name_1, move1)
            if play2.gameover():
                self.result.set("Game Over!")
                self.master.update()
                self.gameover()

            else:
                self.result.set("It's your turn.")
                self.enableButtons()

    
    def DisplayBoard(self):
        """
        Set up the display board canvas, which includes the who's turn it currently is, player1's decision once the game is over and the final statistics.
        """
        Displaylabel = tk.Label(self.master, text="Tic Tac Toe - Display Board ", width=25)
        Displaylabel.grid(row=6, column=1, padx=10, pady=5)

        displayboard = tk.Frame(self.master, width=250, height=250, bg='white')

        self.ResultLabel(displayboard)

        self.player1decision(displayboard)

        self.displayStats(displayboard)
        
        displayboard.grid(row=7, column=1,pady=5, padx=10)


    def ResultLabel(self,displayboard):
        """
        Display the game progress, displaying who's turn it currently is or the game is over..

        Args:
            displayboard: the frame to display the information of the game.
        """
        ResultLabel = tk.Label(displayboard, text="Game progress： ", width=15)
        ResultLabel.grid(row=0, column=0, pady=5, padx=10)
        
        GameResult = tk.Label(displayboard, textvariable=self.result, width=30)
        GameResult.grid(row=0, column=1, pady=5, padx=10)


    def player1decision(self,displayboard):
        """
        Display player1's decision of whether to play again or not.

        Args:
            displayboard: the frame to display the information of the game.
        """
        self.Player1Decision = tk.Label(displayboard,text= "Decision received:",width=15)
        self.Player1Decision.grid(row=1, column=0, pady=5, padx=10)

        self.decisionLabel = tk.Label(displayboard, textvariable=self.decision, width=30)
        self.decisionLabel.grid(row=1, column=1, pady=5, padx=10)


    def displayStats(self,displayboard):
        """
        Display the the final statistics of the game when player1 do not want to play again.

        Args:
            displayboard: the frame to display the information of the game.
        """
        StatsLabel = tk.Label(displayboard, textvariable = self.statistics, width=40)
        StatsLabel.grid(row=2, columnspan = 2, pady=5, padx=10)
        

    def gameover(self):
        """
        Define the command when the game is over:
        if player1 chooses to play again, then reset the board;
        else, end the game.
        """
        self.decision.set(f"Waiting {user_name_1}'s decision...")
        self.master.update()

        self.game_over.set(True)
        decision = self.clientSocket.recv(2014).decode("ascii")
        self.decision.set(decision)

        if decision == "Fun Times":

            self.decision.set("Fun Times! Game End.")
            self.disableButtons()
            self.statistics.set(play2.displayStats())

        elif decision == "Play Again":
            
            self.game_over.set(False)
            self.decision.set("Play Again!")
            self.master.update()
            self.resetButtons()


if __name__=="__main__":
    game = UserInterface2()
    game.master.mainloop()
