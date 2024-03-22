 
pos1 = " "
pos2 = " "
pos3 = " "
pos4 = " "
pos5 = " "
pos6 = " "
pos7 = " "
pos8 = " "
pos9 = " "

turn_text = None
turn_choice = None
X_or_O = None
endgame = False
count = 0
starting_player = None
lost_turn = False


def print_board(): 
    print(f"""
   
     |     |
  {pos1}  |  {pos2}  |  {pos3}  
 ____|_____|_____
     |     |
  {pos4}  |  {pos5}  |  {pos6}  
 ____|_____|_____
     |     |
  {pos7}  |  {pos8}  |  {pos9}  
     |     |

      """)

    return


# Main below here

while starting_player != "X" or "O":
    starting_player = input("Hello! Will X or O start?")
    if starting_player == "X": 
        X_or_O = "X"

    elif starting_player == "x":
        X_or_O = "X"

    elif starting_player == "O":
        X_or_O = "O"

    elif starting_player == "o":
        X_or_O = "O"
    
    else:
        print("Invalid! Please enter X or O")
    if starting_player == "X":
        break
    if starting_player == "O":
        break
    if starting_player == "x":
        break
    if starting_player == "o":
        break
    

while not endgame:

    turn_text = f"{X_or_O} TURN: Where to go?"
    turn_choice = input(f"{turn_text}")


    if turn_choice == "1" and pos1 == " ":
        pos1 = X_or_O
    elif turn_choice == "2" and pos2 == " ":
        pos2 = X_or_O
    elif turn_choice == "3" and pos3 == " ":
        pos3 = X_or_O
    elif turn_choice == "4" and pos4 == " ":
        pos4 = X_or_O
    elif turn_choice == "5" and pos5 == " ":
        pos5 = X_or_O
    elif turn_choice == "6" and pos6 == " ":
        pos6 = X_or_O
    elif turn_choice == "7" and pos7 == " ":
        pos7 = X_or_O
    elif turn_choice == "8" and pos8 == " ":
        pos8 = X_or_O
    elif turn_choice == "9" and pos9 == " ":
        pos9 = X_or_O
    else:
        print("\nInvalid! This position is already taken or you didn't enter 'X' or 'O'.")
        continue
    count += 1

    if X_or_O == "X": 
        X_or_O = "O"
    else:
        X_or_O = "X"





    ##calculates all possible winning positions

    if pos1 == pos2 and pos2 == pos3 and pos1 != " ":
        print("Hooray! You win!")
        endgame = True 

    if pos4 == pos5 and pos5 == pos6 and pos5 != " ":
        print("Hooray! You win!")
        endgame = True 

    if pos7 == pos8 and pos8 == pos9 and pos8 != " ":
        print("Hooray! You win!")
        endgame = True 

    if pos1 == pos4 and pos4 == pos7 and pos7 != " ":
        print("Hooray! You win!")
        endgame = True

    if pos2 == pos5 and pos5 == pos8 and pos2 != " ":
        print("Hooray! You win!")
        endgame = True

    if pos3 == pos6 and pos6 == pos9 and pos6 != " ":
        print("Hooray! You win!")
        endgame = True 

    if pos1 == pos5 and pos5 == pos9 and pos5 != " ":
        print("Hooray! You win!")
        endgame = True 
    if pos3 == pos5 and pos5 == pos7 and pos3 != " ":
        print("Hooray! You win!")
        endgame = True 

    print(f"\n\n Moves:{count}")
    print_board()
