import random
import os


def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

def show_score(score):
    if score < 999:
        print("-" * 35)
        print("---------- High Score: {} ----------".format(score))

def round_guess(rounds, tries):
    print("-" * 35)
    print("Round: {} | Guesses: {}".format(rounds, tries))
    print("-" * 35)

def hint(tries, input, random):
    if tries > 0:
        if input < random:
            print("\nIt's higher than {}, please try again".format(input))
        elif input > random:
            print("\nIt's lower than {}, please try again".format(input))

def finish(rounds, score):
    clear_screen()
    print("#" * 53)
    print("#### Rounds completed: {} | Your High Score is: {} ####".format(rounds, score))
    print("#" * 53)
    print("\n--- Thank you for playing! ---\n")


def start_game():

    random_num = random.randint(1, 10)
    try_count = 0
    round_num = 1
    high_score = 999
    input_user = None
       
    clear_screen()
    print("--- Welcome to the number guessing game ---\n")
    print("Please enter a number between 1 and 10, good luck!\n")

    while True:
        show_score(high_score)
        round_guess(round_num, try_count)

        try:
            hint(try_count, input_user, random_num)
            input_user = int(input("\nWhat is your guess?\n  >  "))
            if input_user > 10 or input_user < 1:
                raise ValueError
        except ValueError:
            clear_screen()
            print("\n>>> Ups! That didn't work, please put in a number between 1 and 10 <<<\n")
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
                finish(round_num, high_score)
                break

if __name__ == '__main__':
    start_game()
