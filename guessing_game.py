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

    random_num = random.randint(1, 10)
    try_count = 0
    round_num = 1
    high_score = 999

    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def show_score():
        if high_score < 999:
            print("-" * 35)
            print("---------- High Score: {} ----------".format(high_score))

    def round_guess():
        print("-" * 35)
        print("Round: {} | You guessed: {} times".format(round_num, try_count))
        print("-" * 35)

    def hint():
        if try_count > 0:
            if input_user < random_num:
                print("\nThe number is higher than {}, please try again \n".format(input_user))
            elif input_user > random_num:
                print("\nThe number is lower than {}, please try again \n".format(input_user))

    def finish():
        clear_screen()
        print("#" * 31)
        print("#### Your High Score is: {} ####".format(high_score))
        print("#" * 31)
        print("\n--- Thank you for playing! ---\n")
       
    clear_screen()
    print("--- Welcome to the number guessing game ---")

    while True:
        show_score()
        round_guess()

        try:
            hint()
            input_user = int(input("What is your guess?\n >   "))
            if input_user > 10:
                raise ValueError
        except ValueError as err:
            clear_screen()
            print(" >>> You have to put in a number between 1 and 10 <<<")
            continue

        if input_user < random_num:
            clear_screen()
            try_count += 1
            continue
        
        elif input_user > random_num:
            clear_screen()
            try_count += 1
            continue

        elif input_user == random_num:
            if high_score > try_count:
                high_score = try_count + 1
            print("-------You got it!-------")
            new_round = input("Want to play again? Y/N >  ")
            if new_round.upper() == "Y":
                try_count = 0
                random_num = random.randint(1, 10)
                round_num += 1
                clear_screen()
                continue
            else:
                finish()
                break





if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
