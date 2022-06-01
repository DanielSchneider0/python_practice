import random
from turtle import clear
from art import logo, vs
from game_data import data


def format_data(account):
    name = account["name"]
    country = account["country"]
    description = account["description"]
    return f"{name}, from {country}, is a {description}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_continue = True
account_b = random.choice(data)

# def random_account():
#     return random.choice(data)
while game_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")

    print(vs)

    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type A or B ").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers, b_followers)

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"Correct, current score: {score}")
    else:
        game_continue = False
        print(f"Incorrect, you're final score: {score}")
