print("Welcome to tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
amount_per_person = bill * (1 + tip / 100) / people
print(f"Each person should pay: ${round(amount_per_person, 2)}")
