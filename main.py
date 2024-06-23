# imported choice method, so I can pick a random element in an array (used in "get_computer_move"
from random import choice


# function that generates a random move (rock, paper or scissors) for the computer
def get_computer_move():
    moves = ["r", "p", "s"]
    return choice(moves)
# function the prompts the user for a move (has to be valid too)
def get_user_move():
    while True:
        move = input("Chose your move! r-rock | p-paper | s-scissors - ").lower()
        if move in ["r", "p", "s"]:
            break
        print("Invalid input, try again")
    return move

# function that checks who the winner is
# prints the moves picked for each side
# also prints who won, who lost and if draw
def check_winner(computer, player):
    current_move = (computer, player)

    losing_message = "Unlucky, the computer won this round"
    losing_options = [("r", "s"), ("s", "p"), ("p", "r")]

    draw_message = "It's a draw!"
    draw_options = [("r", "r"), ("s", "s"), ("p", "p")]

    winning_message = "Nice! You won this round"

    moves = {"r" : "ROCK", "s" : "SCISSORS", "p": "PAPER"}
    show_moves = (f"Your move = {moves[player]} | Computer move = {moves[computer]}")

    if current_move in losing_options:
        print(show_moves)
        print(losing_message)
        return 1
    if current_move in draw_options:
        print(show_moves)
        print(draw_message)
        return 2
    else:
        print(show_moves)
        print(winning_message)
        return 0


# function that makes the game start
def game():
    print("Welcome To My Game!", end="")
    input("")
    print("This is the famous Rock-Paper-Scissors game", end="")
    input("")
    print("In this program, you will compete against the computer", end="")
    input("")
    print("The game is first to 3, meaning first to get to 3 wins, will win", end="")
    input("")
    print("Are you ready?", end="")
    input("")
    computer_wins = 0
    user_wins = 0
    while True:
        user_move = get_user_move()
        computer_move = get_computer_move()
        winner = check_winner(computer_move, user_move)
        if winner == 0:
            user_wins += 1
        if winner == 1:
            computer_wins += 1

        print(f"SCORES: YOU = {user_wins} | COMPUTER = {computer_wins}")

        if computer_wins == 3 or user_wins == 3:
            break

    if user_wins == 3:
        print("Congrats, you defeated the computer!")
    else:
        print(":/ You lost")


if __name__ == "__main__":
    game()

