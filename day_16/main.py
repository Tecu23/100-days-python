from CoffeeMachine import CoffeeMachine



def main():

    coffee_machine = CoffeeMachine(300, 200, 100)

    while True:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if coffee_type == 'off':
            break

        if coffee_type == 'report':
            coffee_machine.print_report()
            continue

        if coffee_type != "espresso" and coffee_type != "latte" and coffee_type != "cappuccino":
            print("Wrong input! Try again.")
            continue

        are_enough_resources, ingredient = coffee_machine.are_resources_sufficient(coffee_type)

        if not are_enough_resources:
            print(f"Sorry there is not enough {ingredient}")
            continue


        is_payment_successful = coffee_machine.process_coins(coffee_type)

        if is_payment_successful:
            coffee_machine.make_coffee(coffee_type)
        else:
            print("Sorry that's not enough money. Money refunded.")












if __name__ == "__main__":
    main()