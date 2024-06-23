from random import choice

# generate a random move for the computer
def get_computer_move():
    moves = ["r", "p", "s"]
    return choice(moves)

def get_user_move():
    while True:
        move = input("Chose your move! r-rock | p-paper | s-scissors - ").lower()
        if move in ["r", "p", "s"]:
            break
        print("Invalid input, try again")
    return move

def check_winner(computer, player):
    dict = {"r" : "ROCK", "s" : "SCISSORS", "p": "PAPER"}
    if computer == "r":
        if player == "s":
            print(f"Your move = {dict[player]} | Computer move = {dict[computer]}")
            print("Unlucky, the computer won this round")
            return 1
        if player == "p":
            print(f"Your move = {dict[player]} | Computer move = {dict[computer]}")
            print("Nice! You won this round")
            return 0
        if player == "r":
            print(f"Your move = {dict[player]} | Computer move = {dict[computer]}")
            print("It's a draw")
            return 2
    if computer == "p":
        if player == "r":
            print(f"Your move = {dict[player]} | Computer move = {dict[computer]}")
            print("Unlucky, the computer won this round")
            return 1
        if player == "s":
            print(f"Your move = {dict[player]} | Computer move = {dict[computer]}")
            print("Nice! You won this round")
            return 0
        if player == "p":
            print(f"Your move = {dict[player]} | Computer move = {dict[computer]}")
            print("It's a draw")
            return 2
    if computer == "s":
        if player == "p":
            print(f"Your move = {dict[player]} | Computer move = {dict[computer]}")
            print("Unlucky, the computer won this round")
            return 1
        if player == "r":
            print(f"Your move = {dict[player]} | Computer move = {dict[computer]}")
            print("Nice! You won this round")
            return 0
        if player == "s":
            print(f"Your move = {dict[player]} | Computer move = {dict[computer]}")
            print("It's a draw")
            return 2


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

        if computer_wins == 3:
            break
        if user_wins == 3:
            break

    if user_wins == 3:
        print("Congrats, you defeated the computer!")
    else:
        print(":/ You lost")


game()

