import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

w = input("Enter the width of the wall: ")
h = input("Enter the height of the wall: ")
coverage = input("How much coverage does one can of paint have (in square meters)?: ")

if w.isdigit() and h.isdigit() and coverage.isdigit():
    width = int(w)
    height = int(h)
    coverage = int(coverage)
    paint_calc(height=height, width=width, cover=coverage)
else:
    print("Please enter valid integer values for width, height, and coverage.")
