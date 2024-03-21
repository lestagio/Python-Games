import random
import time

action_txt = None

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

while True:
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
    elif choice == "rock":
        if computer_choice == "scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_game = input("Would you like to play again? (y/n):")
    if play_game.lower() != "y":
         
        break
