from art import logo

print (logo)

alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.isalpha():  # Check if character is an alphabet or not
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is: {end_text}")


should_continue = True
while should_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction != 'encode' and direction != 'decode':
        print("Invalid input. Please type 'encode' or 'decode'.")
        continue

    text = input("Enter your text: ").lower()

    shift_input = input("Enter shift amount (an integer): ")
    if not shift_input.isdigit():
        print("Shift amount must be a valid integer.")
        continue

    shift = int(shift_input) % 26  # Ensure shift is within the range of the alphabet

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again or type anything else to exit.\n").lower()
    if restart != 'yes':
        should_continue = False
        print("Goodbye!")
