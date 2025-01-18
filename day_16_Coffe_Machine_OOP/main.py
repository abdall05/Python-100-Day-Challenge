from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    client_choice = input(f"What do u want to order ({menu.get_items()}) ? ").lower()
    if client_choice == "off":
        is_on = False
    elif client_choice == "report":
        coffee_maker.report()
    elif menu.find_drink(client_choice):
        order = menu.get_item(client_choice)
        if coffee_maker.is_resource_sufficient(order):
            payment_succeeded = money_machine.make_payment(order.cost)
            if payment_succeeded:
                coffee_maker.make_coffee(order)
