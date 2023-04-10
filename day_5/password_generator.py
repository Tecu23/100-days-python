import random
import string

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like? "))
number_of_digits = int(input("How many numbers would you like? "))

password = ""
symbols = '!@#$%^&*()_'

for letter in range(number_of_letters):
  password += random.choice(string.ascii_letters)

for symbol in range(number_of_symbols):
  password += random.choice(symbols)

for number in range(number_of_digits):
  password += random.choice(string.digits)

password_list = list(password)

random.shuffle(password_list)
               
print(f"Your generated password is {''.join(password_list)}")
