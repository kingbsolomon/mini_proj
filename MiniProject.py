import random

gameType = {
    "Easy": 10,
    "Medium": 100,
    "Hard": 1000,
    "Extreme": 10_000,
    "Insane": 100_000,
    "Hell": 1_000_000
}
guesses = []
curr_guess = -1
generated_num = 0


def generate_num(randMax):
    rand = random.randint(1, randMax)
    print(rand)
    return rand


def is_previous_guess(guess):
    if guess in guesses:
        return True
    else:
        return False


def validate_input():
    choice = input(f"Guess A Number: ")
    try:
        input_to_int = int(choice)
        return input_to_int
    except ValueError:
        print("Not A Valid Number!")
        validate_input()


def validate_difficulty():
    choice = input(f"Choose a Difficulty Level {gameType.keys()}: ")
    if choice in gameType.keys():
        return choice
    else:
        validate_difficulty()


def welcome():
    print("Welcome to Guess the Number\nSelect a difficulty and start guessing\n"
          "You can enter 0 to quit anytime")


def play_again():
    global curr_guess, guesses, generated_num
    again = input("Would you like to play again? Y or N")
    if again == 'Y' or 'y':
        curr_guess = -1
        guesses = []
        generated_num = 0
        run_game()
    else:
        print("Thanks for Playing")


def run_game():
    global curr_guess, generated_num
    welcome()
    max_num = gameType[validate_difficulty()]
    generated_num = generate_num(max_num)

    while curr_guess != 0 and curr_guess != generated_num:
        temp_guess = validate_input()
        if temp_guess == 0:
            print("Thanks for Playing!")
            break
        elif is_previous_guess(temp_guess):
            print("Already Guessed This! Try again!")
        elif temp_guess != generated_num:
            guesses.append(temp_guess)
            curr_guess = temp_guess
            print("Great Guess! Try Again!")
        else:
            guesses.append(temp_guess)
            curr_guess = temp_guess
            print(f"You guessed the number in {len(guesses)} tries!!")

    play_again()


run_game()
