import random
import os

def start_game():

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
        print("Round: {} | Guesses: {}".format(round_num, try_count))
        print("-" * 35)

    def hint():
        if try_count > 0:
            if input_user < random_num:
                print("\nIt's higher than {}, please try again".format(input_user))
            elif input_user > random_num:
                print("\nIt's lower than {}, please try again".format(input_user))

    def finish():
        clear_screen()
        print("#" * 31)
        print("#### Your High Score is: {} ####".format(high_score))
        print("#" * 31)
        print("\n--- Thank you for playing! ---\n")
       
    clear_screen()
    print("--- Welcome to the number guessing game ---\n")
    print("Please enter a number between 1 and 10, good luck!\n")

    while True:
        show_score()
        round_guess()

        try:
            hint()
            input_user = int(input("\nWhat is your guess?\n  >  "))
            if input_user > 10:
                raise ValueError
        except ValueError as err:
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
                finish()
                break

if __name__ == '__main__':
    start_game()
