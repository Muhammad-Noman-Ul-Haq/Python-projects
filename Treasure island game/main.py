print("Welcome to Treasure Island")
print("You need to find the treasure, fellow traveler")

choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' if you want to wait for a boat or 'swim' if you want to swim across: ").lower()
    
    if choice2 == "wait":
        choice3 = input("A boat arrive and takes you to an island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ").lower()
        
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
elif choice1 == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Enter a valid answer.")
