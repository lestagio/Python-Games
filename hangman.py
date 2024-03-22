import random

def choose_word():
    words = ["hangman", "game", "program", "words", "guessing"]
    return random.choice(words)

def show_word(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    return display

def game():
    word_to_guess = choose_word()
    letters_guessed = []
    attempts_remain = int(input("Enter the number of attempts: "))


    print("Hangman")
    print(show_word(word_to_guess, letters_guessed))

    while attempts_remain > 0:
        guess = input("Please guess a letter: ")

        
        if guess in letters_guessed:
            print("Oops! That letter was already guessed!")
        elif guess in word_to_guess:
            letters_guessed.append(guess)
            correct_text = ["Nice Job!", "Awesome!", "Good guess!", "That letter is in the word!"]
            print(random.choice(correct_text))
        else:
            attempts_remain -= 1
            print("That letter is not in the word.")

        turn_display = show_word(word_to_guess, letters_guessed)
        print(turn_display)

        if turn_display == word_to_guess:
            print("You guessed the word!")
            break
        if attempts_remain == 1:
            print(f"Enter a letter. You have 1 guess left.")
        else:
            print(f"Enter a letter. You have {attempts_remain} guesses left.")

    if attempts_remain == 0:
        print(f"Sorry, you ran out of attempts. The word was '{word_to_guess}'.")


game()
