"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import os

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    random_num = reset_num()

    try_count = reset_count()

    def reset_num():
        random_number = random.randint(1, 10) # Muss eine neue Nummer erzeugen wenn man ein neues Spiel startet
        return random_number

    def reset_count():
        count = 0
        return count

    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")



    print("--- Welcome to the number guessing game ---")

    while True:

        print("You guessed: {} times".format(try_count))

        input_user = int(input("What is your guess? >  "))

        if input_user < random_num:
            print("The number is higher than {}, please try again".format(input_user))
            try_count += 1
            continue
        
        elif input_user > random_num:
            print("The number is lower than {}, please try again".format(input_user))
            try_count += 1
            continue

        elif input_user == random_num:
            print("You got it!")
            new_round = input("Want to play again? Y/N >  ")
            if new_round.upper() == "Y":
                print("Your score: {} times guessed".format(try_count))
                continue
            else:
                break
    
    print("Thank you for playing! Your lowest score is: {}".format(try_count))




if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
