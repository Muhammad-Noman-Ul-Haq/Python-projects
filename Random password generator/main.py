import random

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password_chars = [
    random.choice(letters) for _ in range(nr_letters)
] + [
    random.choice(symbols) for _ in range(nr_symbols)
] + [
    random.choice(numbers) for _ in range(nr_numbers)
]

random.shuffle(password_chars)
password = ''.join(password_chars)

print(f"Your password is: {password}")
