import random

EASY_TURNS = 10
HARD_TURNS = 5


def check_answer(guess, selected_number, guesses_remaining):
    if guess < selected_number:
        print("Guess is too low.")
        return guesses_remaining - 1
    elif guess > selected_number:
        print("Guess is too high.")
        return guesses_remaining - 1
    else:
        print(f"Winner. You guessed the number! {selected_number}")


def set_difficulty():
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_TURNS
    elif difficulty == "hard":
        return HARD_TURNS
    else:
        print("Not a valid difficulty")


def play():
    print("Welcome to the Number Guessing Game")
    print("I'm guessing a number between 1 and 100.")
    selected_number = random.randint(1, 100)
    guesses_remaining = set_difficulty()
    guess = 0
    while guess != selected_number:
        print(f"You have {guesses_remaining} guesses remaining to guess the number.")
        guess = int(input(f"Make a guess: "))

        guesses_remaining = check_answer(guess, selected_number, guesses_remaining)
        if guesses_remaining == 0:
            print("You lose.")
            return
        elif guess != selected_number:
            print("Go again")


play()
