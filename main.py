GAME_STATE = True

game_board = [" " for x in range(9)]

def print_board():
    print("\n")
    row_1 = "{}|{}|{}".format(game_board[0], game_board[1], game_board[2])
    row_2 = "{}|{}|{}".format(game_board[3], game_board[4], game_board[5])
    row_3 = "{}|{}|{}".format(game_board[6], game_board[7], game_board[8])
    row_divider = "-----"
    print(row_1)
    print(row_divider)
    print(row_2)
    print(row_divider)
    print(row_3)

def player_move(mark):
    if mark == "X":
        player = 1
    elif mark == "O":
        player = 2
    
    while True:
        move = input(f"\nPlayer {player}'s turn. Choose a position (0-8): ")
        if move in "012345678":
            position = int(move)
            if game_board[position] == " ":
                game_board[position] = mark
                break
            else:
                print("\nThat position is already taken. Please choose another position.\n")
        else:
            print("\nInvalid input. Please enter a number between 0 and 8.\n")

def check_win(mark):
    if (game_board[0] == mark and game_board[1] == mark and game_board[2] == mark) or \
       (game_board[3] == mark and game_board[4] == mark and game_board[5] == mark) or \
       (game_board[6] == mark and game_board[7] == mark and game_board[8] == mark) or \
       (game_board[0] == mark and game_board[3] == mark and game_board[6] == mark) or \
       (game_board[1] == mark and game_board[4] == mark and game_board[7] == mark) or \
       (game_board[2] == mark and game_board[5] == mark and game_board[8] == mark) or \
       (game_board[0] == mark and game_board[4] == mark and game_board[8] == mark) or \
       (game_board[2] == mark and game_board[4] == mark and game_board[6] == mark):
        return True
    else:
        return False

def player_choice():
    choice = input("\nDo you want to play again? (y/n): ")
    if choice.lower() == "y":
        return True
    else:
        return False

def reset_board():
    global game_board
    game_board = [" " for x in range(9)]

while GAME_STATE == True:
    print_board()
    player_move("X")
    print_board()
    if check_win("X"):
        print("\nPlayer 1 wins!\n")
        player_choice()
        if player_choice() == True:
            reset_board()
        elif player_choice() == False:
            GAME_STATE = False
        
    elif " " not in game_board:
        print("\nTie!\n")
        player_choice()
        if player_choice() == True:
            reset_board()
        elif player_choice() == False:
            GAME_STATE = False
        
    player_move("O")
    if check_win("O"):
        print_board()
        print("\nPlayer 2 wins!\n")
        player_choice()
        if player_choice() == True:
            reset_board()
        elif player_choice() == False:
            GAME_STATE = False
