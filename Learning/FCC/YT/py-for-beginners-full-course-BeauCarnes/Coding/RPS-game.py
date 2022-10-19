import random

# variables/functions
def get_choice():
    player_choice = input("Enter a choice (rock | paper | scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    # print("You chose " + player + ", computer chose " + computer)
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a TIE!"
    elif player == "":
        if computer == "scissors":
            return "Rock smashes scissors! You WIN!!"
        else:
            return "Paper covers rock! You Lose!!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You WIN!!"
        else:
            return "Scissors cuts paper! You Lose!!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You Win!!"
        else:
            return "Rock smashes scissors! You Lose!!"


choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)
