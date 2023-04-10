print("Welcome to the tip calculator.\n")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

bill_value = total_bill * (1 + tip_percentage / 100) / number_of_people

print(f"Each person should pay: ${round(bill_value, 2)}")