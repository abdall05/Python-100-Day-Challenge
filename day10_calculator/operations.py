def operation_input():
    while True:
        operation = input("Enter an operation: '+', '/', '-', '*' ")
        if operation in ["+", '/', '-', "*"]:
            return operation
        else:
            print("Invalid operation. Please try again.")


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return first / second


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def compute(first_number, second_number, operation):
    operation_function = operations[operation]
    return operation_function(first_number, second_number)

