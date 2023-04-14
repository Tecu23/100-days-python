from constants import MENU, resources

def print_report(resources):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")

def are_resources_sufficient(coffee_type, resources):        
    if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
        return (False, "water")
    
    if resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        return (False, "milk")
    
    if resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        return (False, "coffee")
    
    return (True, "")

def process_coins(coffee_type):

    print("Please insert coins.")
    quarter_number = int(input("How many quarters?: "))
    dimes_number = int(input("How many dimes?: "))
    nickels_number = int(input("How many nickels?: "))
    pennies_number = int(input("How many pennies?: "))

    total_sum = 0.25 * quarter_number + 0.1 * dimes_number + 0.05 * nickels_number + 0.01 * pennies_number

    if total_sum < MENU[coffee_type]["cost"]:
        return False

    change = total_sum - MENU[coffee_type]["cost"]

    print(f"Here is ${round(change, 1)} in change.")

    return True


def make_coffee(coffee_type, resources):

    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    resources["money"] += MENU[coffee_type]["cost"]

    print(f"Here is you {coffee_type}. Enjoy!")



def main():
    while True:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if coffee_type == 'off':
            break

        if coffee_type == 'report':
            print_report(resources)
            continue

        if coffee_type != "espresso" and coffee_type != "latte" and coffee_type != "cappuccino":
            print("Wrong input! Try again.")
            continue

        are_enough_resources, ingredient = are_resources_sufficient(coffee_type, resources)

        if not are_enough_resources:
            print(f"Sorry there is not enough {ingredient}")
            continue


        is_payment_successful = process_coins(coffee_type)

        if is_payment_successful:
            make_coffee(coffee_type, resources)
        else:
            print("Sorry that's not enough money. Money refunded.")



if __name__ == "__main__":
    main()