import math

# Function with no parameters
def greet():
    print(f"Hello my friend.")
    print("How do you do?")
    print("Isn't the weather nice today?")

# Calling the function with no arguments
greet()

# Function with 1 parameter
def greet_with_name(name):
    print(f"Hello my friend, {name}")
    print(f"How do you do, {name}?")
    print("Isn't the weather nice today?")

# Calling function with 1 argument, the name
greet_with_name("Andrei")

# Function with 2 parameter
def greet_with_name_and_location(name="Max", location="Slobozia"):
    print(f"Hello my friend, {name}")
    print(f"what is like in {location}?")

# Calling function with 2 arguments, the name and the location
greet_with_name_and_location(name="Andrei", location="Bucharest")

# Exercise -> Paint Area Calculator
def paint_area(width, height, coverage):
    return math.ceil((width * height) / coverage)

print(paint_area(width=3, height=9, coverage=5))

# Exercise -> Prime Number Checker
def check_prime(number):

    for i in range(2, round(math.sqrt(number))):
        if number % i == 0:
            print("Not Prime")
            return;

    print("Prime")

check_prime(213970321)