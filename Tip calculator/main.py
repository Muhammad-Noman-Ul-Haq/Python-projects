print("Welcome to the tip calculator!")
bill = float(input("What is the total amount of the bill?\n"))
people = input("how many people are splitting this bill?\n")
tip = input("What percentage tip would you like to give?\n")
tip_percent = float(tip) / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
per_person = round(total_bill / int(people), 2)
print(f"Each person should pay {per_person}")
