def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" ".join(row))


def check_winner(board):
    """Checks if there is a winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]  # Players X and O

    # Loop for a maximum of 9 turns (3x3 board)
    for turn in range(9):
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        # Get valid row and column input
        while True:
            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter column (1-3): ")) - 1
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. The cell is already taken or out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers between 1 and 3.")

        # Update the board with the player's move
        board[row][col] = player

        # Check if there's a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return

    # If all cells are filled and no winner, it's a draw
    print_board(board)
    print("It's a draw!")


# Run the game
tic_tac_toe()
