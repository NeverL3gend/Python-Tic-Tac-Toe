#### 
# This is going to be the start of my first project


board = ["-","-","-",
        "-","-","-",
        "-","-","-"
        ]

current_Player = "x"
winner = None
gameRunning = True


#printing a game board
def printBoard(board):
    print (board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print (board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print (board[6] + "|" + board[7] + "|" + board[8])


#take player input
def player_Input(board):
    inp = int(input("Enter a number 1 through 9: "))
        #first we're confirming if the number is valid from 1 through 9
        # Then we also confirm if the spot is taken or not
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        #from here we're setting the current position
        board[inp-1] = current_Player
    else:
        print ("spot has been played!")

#check for win or tie
def check_Horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[7] and board[6] != "-":
        winner = board[6]
        return True

def check_Vertical (board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[5] and board[7] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_Diagonal (board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[3]
        return True

def tie (board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

def check_winner():
    global gameRunning
    if check_Diagonal(board) or check_Horizontal(board) or check_Vertical(board):
        print(f"The winner {winner}")
        gameRunning = False
#switch the player
def switch_player ():
    global current_Player
    if current_Player == "x":
        current_Player = "O"
    else:
        current_Player = "x"



#check for win or tie again
while gameRunning:
    printBoard(board)
    player_Input(board)
    check_winner()
    tie(board)
    switch_player()