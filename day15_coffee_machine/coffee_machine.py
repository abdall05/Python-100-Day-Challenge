from machine_data import MENU, resources, coins, commands
from ascii_art import logo


def print_logo():
    print(logo)


def prompt_user():
    while True:
        user_input = input("What would you like? (expresso/latte/cappuccino):").lower()
        if user_input in commands:
            return user_input
        else:
            print("That's not a valid command.\nTry again!")


def print_report():
    print(
        f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: {resources["money"]}$')


def get_required_resource(order):
    required_resources = MENU[order]["ingredients"]
    return required_resources


def get_order_cost(order):
    return MENU[order]["cost"]


def check_resources(required_resources):
    is_enough = True
    for resource in required_resources:
        if required_resources[resource] > resources[resource]:
            is_enough = False
            print(f"Sorry there is not enough {resource}.")
    return is_enough


def process_coins():
    print("Please insert coins!")
    money_inserted = 0
    for coin in coins:
        number_of_coins = int(input(f"How many {coin}? "))
        money_inserted += coins[coin] * number_of_coins
    return money_inserted


def check_transaction(order, money_inserted):
    order_price = get_order_cost(order)
    if order_price > money_inserted:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif order_price < money_inserted:
        change = money_inserted - order_price
        print(f"Here is ${round(change, 2)} dollars in change.")
    resources["money"] += order_price
    return True


def make_coffee(order):
    required_resources = get_required_resource(order)
    for resource in required_resources:
        resources[resource] -= required_resources[resource]
    print(f"Here's your {order}.Enjoy!")
