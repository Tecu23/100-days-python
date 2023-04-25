from constants import MENU

class CoffeeMachine:
    
    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = 0
    

    def print_report(self):
        print(f"Water: {self.water}")
        print(f"Milk: {self.milk}")
        print(f"Coffee: {self.coffee}")
        print(f"Money: {self.money}")

    def are_resources_sufficient(self, coffee_type):
        if self.water < MENU[coffee_type]["ingredients"]["water"]:
            return (False, "water")

        if self.milk < MENU[coffee_type]["ingredients"]["milk"]:
            return (False, "milk")

        if self.coffee < MENU[coffee_type]["ingredients"]["coffee"]:
            return (False, "coffee")

        return (True, "")

    def process_coins(self, coffee_type):
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

    def make_coffee(self, coffee_type):

        self.water -= MENU[coffee_type]["ingredients"]["water"]
        self.milk -= MENU[coffee_type]["ingredients"]["milk"]
        self.coffee -= MENU[coffee_type]["ingredients"]["coffee"]
        self.money += MENU[coffee_type]["cost"]

        print(f"Here is you {coffee_type}. Enjoy!")

