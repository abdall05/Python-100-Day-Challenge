import coffee_machine

on = True

coffee_machine.print_logo()

while on:
    user_choice = coffee_machine.prompt_user()
    if user_choice == 'off':
        on = False
    elif user_choice == 'report':
        coffee_machine.print_report()
    else:
        order = user_choice
        required_resources = coffee_machine.get_required_resource(order)
        is_enough_resource = coffee_machine.check_resources(required_resources)
        if is_enough_resource:
            money_inserted = coffee_machine.process_coins()
            transaction_success = coffee_machine.check_transaction(order, money_inserted)
            if transaction_success:
                coffee_machine.make_coffee(order)
