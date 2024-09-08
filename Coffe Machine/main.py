import os
class Coffee:
    """ A generic coffee machine """

    def __init__(self, coffee, cups, water, milk, sugar):
        self.coffee = coffee
        self.cups = cups
        self.water = water
        self.milk = milk
        self.sugar = sugar

    def coffee_maker(self):
        preferred_coffee = type_of_coffee()
        sugar_intake = some_sugar()
        if sugar_intake in ("Y", "y"):
                self.sugar -= 5

        if preferred_coffee == 1:
            print("Espresso coming up!\n")
            print("1 Espresso delivered!")

        elif preferred_coffee == 2:
            print("Filtered Coffee coming up!\n")
            print("1 Filtered Coffee delivered!")

        elif preferred_coffee == 3:
            print("Latte coming up!\n")
            print("1 Latte delivered!")
            self.milk -= 30

        elif preferred_coffee == 4:
            print("Cappuccino coming up!\n")
            print("1 Cappuccino delivered!")
            self.milk -= 30

        self.coffee -= 140
        self.cups -= 1
        self.water -= 120

    def coffee_maker_report(self):  # returns the amount of: coffee, sugar, water, milk, cups left
        return {"Coffee": self.coffee, "Water": self.water, "Milk": self.milk, "Sugar": self.sugar, "Cups": self.cups}


def type_of_coffee():  # this function makes sure the user chooses a their coffee of choice by getting ONLY a valid
    # input
    print("Hi there, what would you like to drink")
    coffee_list = ["1 - Espresso", "2 - Filter", "3 - Cappuccino", "4 - Latte"]

    valid = False
    while not valid:
        try:
            choice = int(input("Enter Choice: "))
            if choice in (1, 2, 3, 4):
                valid = True
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid option")

    return choice


def some_sugar():

    valid = False

    while not valid:
        try:
            choice = input("Some sugar? ")
            if choice in ("Y", "y", "N", "n"):
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")

    return choice


def main():
    os.system("cls")
    new_coffee = Coffee(3500, 25, 3000, 750, 125)  # mg, no., ml, ml, mg
    print(new_coffee.coffee_maker_report())
    new_coffee.coffee_maker()
    print(new_coffee.coffee_maker_report())

