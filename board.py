from pickle import TRUE


board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

def print_board(board):
    for row in board:
        print(row)

def take_turn(playerNumber, playerMark):
    takingTurn = True
    while(takingTurn):
        turnText = "Player {} please take your turn"
        print(turnText.format(playerNumber))
        row = int(input("Enter a row number: "))
        column = int(input("Enter a column number: "))
        playerChoice = [row, column]
        if row > 2 or column > 2:
            print("Please choose a correct location")
        else:
            if not check_markExists(playerChoice):
                takingTurn = False
                place_mark(playerChoice, playerMark)
            else:
                print("That location is taken, please choose a different location")
    

def check_markExists(playerChoice):
    boardLocationX = playerChoice[0]
    boardLocationY = playerChoice[1]
    if board[boardLocationX][boardLocationY] == '_':
        return False
    else:
        return True

def place_mark(playerChoice, playerMark):
    board[playerChoice[0]][playerChoice[1]] = playerMark

def check_win():
    print()

playingGame = True

playerTurn = 1

print(board[0][1])

while playingGame:
    print_board(board)
    if playerTurn == 1:
        playerChoice = take_turn(playerTurn, 'X')       
        playerTurn += 1
    else:
        playerChoice = take_turn(playerTurn, 'O')
        playerTurn -= 1