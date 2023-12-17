# Define board and players
board = [' '] * 9
current_player = 'X'

# Function to display the board
def display_board():
    for i in range(3):
        for j in range(3):
            print(board[i*3 + j], end=" ")
        print()

# Function to check for valid move
def valid_move(move):
    return move >= 0 and move <= 8 and board[move] == ' '

# Function to make a move
def make_move(move, player):
    board[move] = player

# Function to check for win
def check_win(player):
    win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6))
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Game loop
while True:
    display_board()

    # Get player move
    move = int(input(f"{current_player}'s turn, enter a move (1-9): ")) - 1

    # Check for valid move
    if not valid_move(move):
        print("Invalid move, please try again.")
        continue

    # Make the move
    make_move(move, current_player)

    # Check for win or draw
    if check_win(current_player):
        display_board()
        print(f"{current_player} wins!")
        break

    # Check for draw
    if all(x != ' ' for x in board):
        display_board()
        print("It's a draw!")
        break

    # Switch player
    current_player = 'O' if current_player == 'X' else 'X'

# End game
print("Thanks for playing!")

