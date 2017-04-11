import random


# Function to draw the tic tac toe board
def draw_board(board):
    print("")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")  # Top Row
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")  # Middle Row
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")  # Bottom Row


# Function to choose what marker the players would like (X or 0)
def player_marker():
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input("Player 1, please select your marker (x or o): ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Function to decide which player goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Function to place the marker on the board
def place_marker(board, marker, position2):
    board[position2 - 1] = marker

# Function to check if a player has won
def check_win(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or  # Top row
            (board[3] == mark and board[4] == mark and board[5] == mark) or  # Middle Row
            (board[6] == mark and board[7] == mark and board[8] == mark) or  # Bottom Row
            (board[0] == mark and board[4] == mark and board[8] == mark) or  # Diagonal left
            (board[2] == mark and board[4] == mark and board[6] == mark) or  # Diagonal right
            (board[0] == mark and board[3] == mark and board[6] == mark) or  # Column Left
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # Column Middle
            (board[2] == mark and board[5] == mark and board[8] == mark))  # Column Right


# Checks to see if space has been played on or not
# Returns boolean
def space_check(board, position):
    for spots in board:
        if spots == str(position):
            return True
    return False


# Checks to see if board is completely full or not (i.e. no integers on board)
def full_board_check(board):
    for spot in board:
        if space_check(board, spot):
            return False  # Board is full
    return True  # Board is not full


# Function to ask where they want to play on the board
def player_choice(board, player_turn):
    position1 = ' '
    while position1 not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, position1):
        position1 = raw_input(player_turn + ", select a spot on the board that corresponds to a number (1-9): ")
    return int(position1)

# Function to ask player to replay
def replay():
    return raw_input("Would you like to play again? [yes/no]: ").lower().startswith("y")


# Actual Game
while True:
    theBoard = '1 2 3 4 5 6 7 8 9'.split()
    player1_marker, player2_marker = player_marker()
    print(player1_marker)
    turn = choose_first()
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player 1 turn

            draw_board(theBoard)
            position = player_choice(theBoard, turn)
            place_marker(theBoard, player1_marker, position)

            if check_win(theBoard, player1_marker):
                draw_board(theBoard)
                print("Player 1 is the winner!")
                game_on = False

            else:
                if full_board_check(theBoard):
                    draw_board(theBoard)
                    print("The game is a tie!")
                    game_on = False
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player 2 turn

            draw_board(theBoard)
            position = player_choice(theBoard, turn)
            place_marker(theBoard, player2_marker, position)

            if check_win(theBoard, player2_marker):
                draw_board(theBoard)
                print("Player 2 is the winner!")
                game_on = False

            else:
                if full_board_check(theBoard):
                    print("The game is a tie!")
                    game_on = False
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
