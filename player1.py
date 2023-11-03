import socket
from gameboard import BoardClass
import tkinter as tk
from tkinter import ttk

class UserInterface1():
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
        self.createConnectButton()
        self.createConnectResultLabel()
        self.createTryAgainButton()
        self.createUserNameEntry()
        self.UserNameLable()
        self.UserName2Lable()
        self.GameBoard()
        self.DisplayBoard()
    
    def initTKVvariables(self):
        """
        Define the initial varialbes.

        Variables:
            self.serverAddress: the server address entered by player1.
            self.serverPort: the port entered by player1.
            self.connection: the result of whether the connection is made successfully or not.
            self.username: the user name of player1 itself.
            self.nameResult: the result of whether the user name entered by player1 is correct or not.
            self.username2: the indication of being received player2's user name successfully or not.
            self.result: the game progress, displaying who's turn it currently is or the game is over.
            self.game_over: True is game is over and False if not.
            self.statistics: the statistics of the game.
        """
        self.serverAddress = tk.StringVar()
        self.serverPort = tk.IntVar()
        self.connection = tk.StringVar()
        self.username = tk.StringVar()
        self.nameResult = tk.StringVar()
        self.username2 = tk.StringVar()
        self.result = tk.StringVar()
        self.game_over = tk.BooleanVar(value=False)
        self.statistics = tk.StringVar(value = "Final Statistics")

        
    def canvasSetup(self):
        """
        Initialize my tkinter canvas.
        """
        self.master = tk.Tk()
        self.master.title("Tic Tac Toe - Player1")
        self.master.geometry("780x600")
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

        
    def connectToServer(self):
        """
        Connect player1 to player2 and display the result of whether the connection is made successfully or not.
        """
        try:
            address = self.serverAddress.get()
            port = self.serverPort.get()
            self.connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connectionSocket.connect((address, port))
            self.connection.set("Connected to server successfully!")
            self.SubmitNameButton.config(state=tk.NORMAL)
        except Exception:
            self.connection.set("Unable to connect to server.")
            self.YesButton.config(state=tk.NORMAL)
            self.NoButton.config(state=tk.NORMAL)
            

    def createTryAgainButton(self):
        """
        Define a try again connect botton on the UI.
        """
        laddress = tk.Label(self.master, text="Whether to try again connecting?")
        laddress.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.YesButton = ttk.Button(self.master,text= "Yes.", command=self.YesTry, state=tk.DISABLED)
        self.YesButton.grid(row=4, column=1, padx=10, pady=5,sticky="w")
        self.NoButton = ttk.Button(self.master,text= "No.", command=self.master.destroy, state=tk.DISABLED)
        self.NoButton.grid(row=4, column=1, padx=5, pady=10)


    def YesTry(self):
        """
        Clear the current adddress, port number, and connection result, and disable the try again button.
        """
        self.serverAddress.set("")
        self.serverPort.set(0)
        self.connection.set("")
        self.YesButton.config(state=tk.DISABLED)
        self.NoButton.config(state=tk.DISABLED)


    def createUserNameEntry(self):
        """
        Define a method that creates a UserName entry file and a button to submit the user name to player2.
        """
        lUserName = tk.Label(self.master, text="Enter the User Name:")
        lUserName.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.UserNameEntry = tk.Entry(self.master, textvariable = self.username)
        self.UserNameEntry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        self.SubmitNameButton = ttk.Button(self.master,text= "Submit the user name to another player.", command=self.UserNameSubmit, state=tk.DISABLED)
        self.SubmitNameButton.grid(row=6, column=0, padx=10, pady=5,sticky="w")


    def UserNameLable(self):
        """
        Display the result of whether the user name entered by player1 is correct or not.
        """
        result_label = tk.Label(self.master, textvariable=self.nameResult, width=25)
        result_label.grid(row=6, column=1, padx=10, pady=5,sticky="w")


    def UserName2Lable(self):
        """
        Display the received user name of Player2.
        """
        result_label = tk.Label(self.master, textvariable=self.username2, width=50)
        result_label.grid(row=7, columnspan=2, pady=5)

  
    def UserNameSubmit(self):
        """
        If the user name is entered correctly, send the name to player2, and receive player2's user name;
        else, clear the user name and prompt player1 to enter a new valid name.
        """
        username = self.username.get()
        if username.isalnum():
            self.connectionSocket.send(username.encode())
            self.nameResult.set("Great! Sending it to another player...")
            self.master.update()
            self.SubmitNameButton.config(state=tk.DISABLED)

            global play1, user_name_1, user_name_2
            
            user_name_2 = self.connectionSocket.recv(1024).decode("ascii")
            self.username2.set(f"Received the user name of another player: {user_name_2}")
            user_name_1 = self.username.get()

            play1 = BoardClass(1, user_name_1, user_name_2)
            self.enableButtons()

            self.result.set("It's your turn! ")
            self.master.update()

        else:
            self.nameResult.set("Please enter a valid user name.")
            self.username.set("")


    def GameBoard(self):
        """
        Set up the game board canvas.
        """
        boardlabel = tk.Label(self.master, text="Tic Tac Toe - PLay Board ", width=25)
        boardlabel.grid(row=8, column=0, padx=10, pady=5)
        gameboard = tk.Frame(self.master, width=250, height=250, bg='white')
        
        self.buttons = [[None, None, None] for _ in range(3)]
        
        for i in range(0,3):
            for j in range(0,3):
                self.setupButton(gameboard,i,j)

        gameboard.grid(row=9, column=0,pady=5, padx=10)


    def setupButton(self,frame, x,y):
        """
        Set up the buttons on the game board.
        """
        button = tk.Button(frame, text="", command=lambda row=x, col=y: self.playboard(row, col), width=8, height=5, state=tk.DISABLED)
        button.grid(row=x, column=y)
        self.buttons[x][y] = button

    
    def playboard(self,row,col):
        """
        Define the button command, where player can click to make the move and the move will be sent to player2.

        Args:
            row: the row of the move made by player1.
            col: the col of the move made by player1.
        """

        if self.game_over.get() == True:
            return # do nothing if the game is over.
        
        button = self.buttons[row][col]
        if button["text"] == "":
            button.configure(text="X")
            self.disableButtons()
            self.result.set(f"Waiting for {user_name_2}'s move...")
            self.master.update()

            move = f"{row+1}{col+1}"
            play1.updateGameBoard(user_name_1, move)
            self.connectionSocket.send(move.encode())

            self.statusCheck()


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
        play1.resetGameBoard()

        
    def statusCheck(self):
        """
        Check the current status of the game:
        if game is over, end the game;
        else, if game is not over, continue the game by letting player2 make the move.
        """
        if play1.gameover(): 
            self.result.set("Game Over!")
            self.master.update()
            self.gameover()

        else: 
            move2 = self.connectionSocket.recv(2014).decode("ascii")

            button = self.buttons[int(move2[0])-1][int(move2[1])-1]
            if button["text"] == "":
                button.configure(text="O")

            play1.updateGameBoard(user_name_2, move2)

            if play1.gameover():
                self.result.set("Game Over!")
                self.master.update()
                self.gameover()
                
            else:
                self.result.set(f"It's your turn.")
                self.enableButtons()


    def gameover(self):
        """
        End the game when game is over by disabling play boaord buttons and asking user whether to play again.
        """
        self.disableButtons()
        self.enableplayagain()
        self.game_over.set(True)
        

    def DisplayBoard(self):
        """
        Set up the display board canvas, which includes the who's turn it currently is, player1's decision once the game is over and the final statistics.
        """
        Displaylabel = tk.Label(self.master, text="Tic Tac Toe - Display Board ", width=25)
        Displaylabel.grid(row=8, column=1, padx=10, pady=5)

        displayboard = tk.Frame(self.master, width=250, height=250, bg='white')

        self.ResultLabelButton(displayboard)
        
        self.PlayAgainButtom(displayboard)

        self.displayStats(displayboard)
        
        displayboard.grid(row=9, column=1,pady=5, padx=10)


    def ResultLabelButton(self,displayboard):
        """
        Display the game progress, displaying who's turn it currently is or the game is over..

        Args:
            displayboard: the frame to display the information of the game.
        """
        ResultLabel = tk.Label(displayboard, text="Game progress： ", width=15)
        ResultLabel.grid(row=0, column=0, pady=5, padx=10)
        
        GameResult = tk.Label(displayboard, textvariable=self.result, width=25)
        GameResult.grid(row=0, column=1, pady=5, padx=10)


    def PlayAgainButtom(self,displayboard):
        """
        Create button to ask user to play again or not.

        Args:
            displayboard: the frame to display the information of the game.
        """
        PlayAgainLabel = tk.Label(displayboard, text="Play Again? ", width=15)
        PlayAgainLabel.grid(row=1, column=0, pady=5, padx=10)
        
        self.YesAgainButton = ttk.Button(displayboard,text= "Yes", command=self.playagainyes,state=tk.DISABLED)
        self.YesAgainButton.grid(row=1, column=1, padx=10, pady=5,sticky="w")

        self.NoAgainButton = ttk.Button(displayboard,text= "No", command=self.playagainno,state=tk.DISABLED)
        self.NoAgainButton.grid(row=1, column=1, padx=10, pady=5,sticky="e")


    def displayStats(self,displayboard):
        """
        Display the the final statistics of the game when player1 do not want to play again.

        Args:
            displayboard: the frame to display the information of the game.
        """
        StatsLabel = tk.Label(displayboard, textvariable = self.statistics, width=40)
        StatsLabel.grid(row=2, columnspan = 2, pady=5, padx=10)
        
    
    def enableplayagain(self):
        """
        Enable play again button.
        """
        self.YesAgainButton.config(state=tk.NORMAL)
        self.NoAgainButton.config(state=tk.NORMAL)

    
    def playagainyes(self):
        """
        Send play again to player2 and reset the game when player1 want to play again.
        """
        self.connectionSocket.send("Play Again".encode())
        self.resetButtons()
        self.game_over.set(False)
        self.enableButtons()
        

    def playagainno(self):
        """
        Send Fun Times to player2, end the game, and display the game statistics.
        """
        self.connectionSocket.send("Fun Times".encode())
        self.YesAgainButton.config(state=tk.DISABLED)
        self.statistics.set(play1.displayStats())
        
        
if __name__=="__main__":
    game = UserInterface1()
    game.master.mainloop()

