from art import logo, vs
from game_data import data
import random
import os

score = 0

A_OPTION = "a"
B_OPTION = "b"

def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess"""
    if a_followers > b_followers:
        return guess == A_OPTION
    else:
        return guess == B_OPTION

def clear():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

game_should_continue = True

print(logo)

while game_should_continue:
    # generate a random choice
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Compare B : {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    while guess not in [A_OPTION, B_OPTION]:
        guess = input("Invalid input. Please type 'A' or 'B': ").lower()

    # check if the user is right or wrong
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)  # True, False

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
