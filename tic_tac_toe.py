board =[                # for the elements of the board
    "-","-","-",
    "-","-","-",
    "-","-","-"
]
current_player="x"
gameRunning=True
winner = None
#getting pichi
# making the game board
def printboard(board):
    print(board[0]+ " | "+board[1]+" | "+board[2]+"\n"+
          "----------"+"\n"+
          board[3]+" | "+board[4]+" | "+board[5]+"\n"+
          "----------"+"\n"+
          board[6]+" | "+board[7]+" | "+board[8])

# taking the input of the player
def position(current_player):
    num=int(input("Enter a position 1-9: "))
    if num>=1 and num<=9 and board[num-1]=="-":
        board[num-1]=current_player
        #printboard(board)
    elif board[num-1]!="-":
        print("Oops! position already chosen")
    else:
        print("Enter a valid position")

# check for win or tie
# using 3 functions 

def check_row(board):
    global winner
    if board[0] == board[1] == board[2] and board[0]!="-":
        winner = board[0]
        return True
    if board[3] == board[4] == board[5] and board[3]!="-":
        winner = board[4]
        return True
    if board[6] == board[7] == board[8] and board[6]!="-":
        winner = board[7]
        return True

def check_col(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!="-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[4]!="-":
        winner = board[4]
        return True
    if board[2] == board[5] == board[8] and board[8]!="-":
        winner = board[8]
        return True

def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!="-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[4]!="-":
        winner = board[4]
        return True

def check_tie(board):
    global gameRunning
    if "-" not in board and not check_row(board) and not check_col(board) and not check_diag(board):
        printboard(board)
        print("It's a tie")
        gameRunning = False
        
def check():
    if check_row(board) or check_col(board) or check_diag(board):
        printboard(board)
        print(winner+ " is the Winner!")
        quit()

# switch the player
def switch(): 
    global current_player
    if current_player=="o":
        current_player="x"
    else:
        current_player="o"

# check for win or tie again


while gameRunning:
    printboard(board)
    position(current_player)
    check()
    check_tie(board)
    switch()


