"""
1. create a program in Python that allows a human to play Tic Tac Toe against a bot by requesting user input
as an array ([row, column]) and prints the board's current state to terminal after each move by either
the human or the bot

2. revise the bot's behavior such that its moves are not simply random, but are instead always an attempt
to thwart the human player (thus creating a stalemate)
"""

import random


# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


# Function to make a bot move
def bot_move(board):
    # Check if the bot can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                if check_win(board, "O"):
                    board[row][col] = " "
                    return row, col
                board[row][col] = " "

    # Check if the human can win in the next move and block it
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                if check_win(board, "X"):
                    board[row][col] = "O"
                    return row, col
                board[row][col] = " "

    # If no winning moves are possible, make a random move
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                available_moves.append([row, col])
    return random.choice(available_moves)


# Initialize the board
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# Main game loop
while True:
    print_board(board)

    # Human's turn
    while True:
        user_input = input("Enter your move (row, column): ")
        row, col = map(int, user_input.split(","))

        if board[row][col] == " ":
            board[row][col] = "X"
            break
        else:
            print("Invalid move. Try again.")

    # Check if the human has won
    if check_win(board, "X"):
        print_board(board)
        print("Congratulations! You won!")
        break

    # Check for a draw
    if all(board[row][col] != " " for row in range(3) for col in range(3)):
        print_board(board)
        print("It's a draw!")
        break

    # Bot's turn
    bot_row, bot_col = bot_move(board)
    board[bot_row][bot_col] = "O"

    # Check if the bot has won
    if check_win(board, "O"):
        print_board(board)
        print("Sorry, you lost. The bot won.")
        break
