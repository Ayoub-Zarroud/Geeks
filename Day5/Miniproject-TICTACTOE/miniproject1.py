# Tic Tac Toe Game in Python
# Two players take turns to mark 'X' or 'O' on a 3x3 board.
# Step 1: Represent the game board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]
# Step 2: Display the game board
def display_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
    print("\n")
# Step 3: Get player input
def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1
            # Validate input range
            if row not in range(3) or col not in range(3):
                print("Invalid position! Choose values between 1 and 3.")
                continue
            # Check if the cell is empty
            if board[row][col] != ' ':
                print("That cell is already taken. Try again.")
                continue

            return row, col
        except ValueError:
            print("Please enter valid numbers.")
# Step 4: Check for a winner
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False
# Step 5: Check for a tie
def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)
# Step 6: Main game loop
def play():
    board = create_board()
    current_player = 'X'
    print("Welcome to Tic Tac Toe!")
    print("Players: X and O")
    display_board(board)
    while True:
        # Get move
        row, col = player_input(board, current_player)
        board[row][col] = current_player
        # Display updated board
        display_board(board)
        # Check winner
        if check_win(board, current_player):
            print(f"Player {current_player} wins! Congratulations!")
            break
        # Check tie
        if check_tie(board):
            print("It's a tie!")
            break
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
# Run the game
if __name__ == "__main__":
    play()
