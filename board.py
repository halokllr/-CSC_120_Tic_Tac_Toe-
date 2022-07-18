from tokenize import String


board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

answerKey = [[[0,0],[0,1],[0,2]],
             [[1,0],[1,1],[1,2]],
             [[2,0],[2,1],[2,2]],
             [[0,0],[1,0],[2,0]],
             [[1,0],[1,1],[1,2]],
             [[2,0],[2,1],[2,2]],
             [[0,0],[1,1],[2,2]],
             [[0,2],[1,1],[2,0]]]

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
                place_mark(playerChoice, playerMark, playerNumber)
            else:
                print("That location is taken, please choose a different location")
    

def check_markExists(playerChoice):
    boardLocationX = playerChoice[0]
    boardLocationY = playerChoice[1]
    if board[boardLocationX][boardLocationY] == '_':
        return False
    else:
        return True

def place_mark(playerChoice, playerMark, playerNumber):
    board[playerChoice[0]][playerChoice[1]] = playerMark
    if playerNumber == 1:
        playerOneAnswers.append(playerChoice)
    else:
        playerTwoAnswers.append(playerChoice)

def check_win(player):
    if player == 1:
        if len(playerOneAnswers) + len(playerTwoAnswers) == 9:
            tie_game()
            quit()
        for key in answerKey:
            if playerOneAnswers == key:
                return True
    else:
        for key in answerKey:
            if playerTwoAnswers == key:
                return True
    return False

def show_winner(playerNumber):
    message = "Player {} wins!"
    print(message.format(playerNumber))

def tie_game():
    print("It's a tie, nobody wins")


playingGame = True
playerTurn = 1

playerOneAnswers = []
playerTwoAnswers = []

while playingGame:
    print_board(board)
    if playerTurn == 1:
        playerChoice = take_turn(playerTurn, 'X')   
        if check_win(playerTurn):
            playingGame = False
            show_winner(playerTurn)
            break
        playerTurn += 1
    else:
        playerChoice = take_turn(playerTurn, 'O')
        if check_win(playerTurn):
            playingGame = False
            show_winner(playerTurn)
            break
        playerTurn -= 1