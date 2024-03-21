#Yay!

import random
import time

action_txt = None
player_score = 0
computer_score = 0

def rock():
    print(f"""

    {action_txt}
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
    return


def paper():
    print(f"""

    {action_txt}
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)


def scissors():
    print(f"""

    {action_txt}
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)


user_inputs = ['r', 'p', 's', 'rock', 'paper', 'scissors']


print("Welcome to Python Rock Paper Scissors! Please choose a mode:\n"
      "Mode 1: Play infinitely until you decide to end the game\n"
      "Mode 2: Play a set amount of rounds against the computer")

mode = input("1 or 2:")

total_games = "999999"
if mode == "2":
    print("How many games would you like to play? - Integer entered should be odd (Best of 3, best of 5, etc)")

    while True:
        total_games = input("Enter an odd integer:")
        if total_games.isdigit() and int(total_games) % 2 != 0:
            break
        else:
            print("Oops! Please enter an odd integer.")
count = 0


while count < int(total_games):
    print("You can type 'r', 'p' or 's' to indicate your choice! ")
    choice = input("Please enter a choice (rock, paper or scissors): ")

    if choice == 'r':
        choice = 'rock'
    elif choice == 'p':
        choice = 'paper'
    elif choice == 's':
        choice = 'scissors'

    if choice in user_inputs:
        print('Good Choice!')
    else:
        print('That is not a valid choice. Please enter another choice.')
        continue

    possible_choice = ("rock", "paper", "scissors",)
    computer_choice = random.choice(possible_choice)

    if choice == "rock":
        action_txt = "You:"
        rock()
    elif choice == "paper":
        action_txt = "You:"
        paper()
    elif choice == "scissors":
        action_txt = "You:"
        scissors()

    if computer_choice == "rock":
        action_txt = "Computer:"
        rock()
    elif computer_choice == "paper":
        action_txt = "Computer:"
        paper()
    elif computer_choice == "scissors":
        action_txt = "Computer:"
        scissors()

    time.sleep(2)
    print(f"You chose {choice}, computer chose {computer_choice}.")

    if choice == computer_choice:
        print("It's a tie!")
        print(f"Your current score: {player_score}, Computer's current score: {computer_score} ")
    elif choice == "rock":
        if computer_choice == "scissors":
            player_score += 1
            print("Rock beats scissors! You win!")
            print(f"Your current score: {player_score}, Computer's current score: {computer_score} ")
        else:
            computer_score += 1
            print("Paper covers rock! You lose.")
            print(f"Your current score: {player_score}, Computer's current score: {computer_score} ")
    elif choice == "paper":
        if computer_choice == "rock":
            player_score += 1
            print("Paper covers rock! You win!")
            print(f"Your current score: {player_score}, Computer's current score: {computer_score} ")
        else:
            computer_score += 1
            print("Scissors cuts paper! You lose.")
            print(f"Your current score: {player_score}, Computer's current score: {computer_score} ")
    elif choice == "scissors":
        if computer_choice == "paper":
            player_score += 1
            print("Scissors cuts paper! You win!")
            print(f"Your current score: {player_score}, Computer's current score: {computer_score} ")
        else:
            computer_score += 1
            print("Rock smashes scissors! You lose.")
            print(f"Your current score: {player_score}, Computer's current score: {computer_score} ")

    count += 1

    if count >= int(total_games):
        print(f"Game total of {total_games} has been reached.")
        print(f"Your final score was: {player_score}. Computer's final score was {computer_score}. ")
    if mode == "1":
        play_game = input("Would you like to play again? (y/n):")
        if play_game.lower() != "y":
            print(f"Your final score was: {player_score}. Computer's final score was {computer_score}. ")
            if player_score < computer_score:
                print("Computer wins!")
            else:
                print("You win!")

            exit()
