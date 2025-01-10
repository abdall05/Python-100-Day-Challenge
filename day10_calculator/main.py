from ascii_art import logo
from operations import operation_input, compute
from utilities import clear

print(logo)

finished = False
accumulate = False
first_number = 0.0
while not finished:
    if not accumulate:
        first_number = float(input("What is the first number? "))
    else:
        print(f"Your first number is {first_number}.")
    operation = operation_input()
    second_number = float(input("What is the second number? "))
    result = compute(first_number, second_number, operation)
    print(f"{first_number} {operation} {second_number} = {result}")
    choice = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or type 'q' to exit: ")
    if choice == "y":
        first_number = result
        accumulate = True
    elif choice == "n":
        accumulate = False
        clear()
    else:
        finished = True
