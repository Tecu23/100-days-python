""" 
  CONDITIONAL STATEMENTS
"""

# If Statements
print("Welcome tot the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

# Comparison Operators >, <, >=, <=, ==, !=


# Exercise -> Odd or Even
number = 10
if number % 2 == 0:
  print("The number you inputed is even.")
else:
  print("The number you inputed is odd.")


# Nested If Statements
age = 17
height = 150

if height > 120:
  if age >= 18:
    print("Pay $12")
  elif age >= 12:
    print("Pay $7")
  else:
    print("Pay $5")
else:
  print("You can't ride")


# Exercise -> BMI Calculator 2.0

height = 1.8
weight = 90

bmi = round(weight / height ** 2)

if bmi < 18.5:
  print("underweight")
elif bmi < 25:
  print("normal weight")
elif bmi < 30:
  print("overweight")
elif bmi < 35:
  print("obese")
else:
  print("clinically obese")

# Exercise -> Leap Year
year = 2000

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap Year")
    else:
      print("Not Leap Year")
  else:
    print("Leap Year")
else:
  print("Not Leap Year")

# Multiple If Statements
sum = 0
height = 180
age = 24
want_photos = True

if height < 120:
  print("You cannot ride")
else:
  if age < 12:
    sum += 5
  elif age < 18:
    sum += 7
  else:
    sum += 12
  
  if want_photos:
    sum += 3

  print(f"Total bill was ${sum}")

# Exercise -> Pizza Order Practice
pizza_size = 'L' # S ($15) or M ($20) or L($25)
pepperoni = True # +2 for S and +3 for L
cheese = True # +1
total = 0

if pizza_size == 'S':
  total += 15
elif pizza_size == 'M':
  total += 20
elif pizza_size == 'L':
  total += 20
else:
  print("Wrong Order")

if pepperoni:
  if pizza_size == 'S':
    total += 2
  else:
    total += 3

if cheese:
  total += 1

print(f"Total ${total}")

# Logical Operators not, and, or, & (and), ^ (xor), | (or)
