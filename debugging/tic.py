def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def get_valid_input(player):
    while True:
        try:
            # Ask for row input
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            if row not in [0, 1, 2]:
                print("Invalid row! Please enter 0, 1, or 2.")
                continue
            
            # Ask for column input
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if col not in [0, 1, 2]:
                print("Invalid column! Please enter 0, 1, or 2.")
                continue
            
            return row, col
        except ValueError:
            print("Invalid input! Please enter numeric values for row and column.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        row, col = get_valid_input(player)
        
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")
    
    print_board(board)
    print(f"Player {player} wins!")

tic_tac_toe()
