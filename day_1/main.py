""" 
    PRINTING
"""

print("Day 1 - Python Print Function \n\
The function is declared like this: \n\
print(\"what to print\")")

# NORMAL CONCATENATION
print("Hello " + "Angela")

# BASIC FORMATTING
print(f"Hello {'Angela'}")

# C LIKE FORMATTING
print("Hello %s" % 'Angela')

# STRING FORMATTING
print("Hello {}".format('Angela'))

# INPUT 
print("Hello " + input ("What is your name ? ") + "!")

# PRINTING THE LENGTH OF THE INPUT STRING
print(len(input("")))

""" 
    VARIABLES
"""
# STRING VARIABLE
name = input("What is your name? ")

print("Hello " + name)

# EXERCISE
a = input("a: ")
b = input("b: ")

aux = a
a = b
b = aux

print(f"a = {a}")
print(f"b = {b}")

