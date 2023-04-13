"""
  DATA TYPES
"""

# String
string = "This is a string"

# first and last character of the string
print(string[0], string[len(string) - 1])

print("123" + "345")

# Integer
integer = 123
long_number = 123_456_789

print(123 + 345)

# Float
pi = 3.14159

# Boolean
true = True
false = False

# TYPE ERROR
  # len(4837) 

# TYPE CHECKING
print(type(integer))

# TYPE CONVERSION
string_integer = str(integer)
float_integer = float(integer)

print("This integer is a string " + string_integer)
print(70 + float("100.5"))
print(str(70) + str(100.5))


# EXERCISE
number = 35
string_number = str(35)

first_digit = string_number[0]
second_digit = string_number[1]

print(int(first_digit) + int(second_digit))
print(number // 10 + number % 10)

# MATHEMATICAL OPERATION
a = 2
b = 3

sum = a + b
difference = a - b
product = a * b
division = a/b
power = a**b
modulo = a % b

print(f"Sum {sum}, Difference {difference}, Product {product}, Division {division}, Power {power}, Modulo {modulo}")

# EXERCISE -> BMI CALCULATOR
weight = 91
height = 1.85

bmi = weight / height**2

print(int(bmi))

# ROUND
print(round(8/3, 2))
print(8//3)

# OPERATORS
score = 0

score += 1
score *= 3
score -= 2
score /= 5

print(score)

score = 0
height = 1.8
isWinning = True

# F String
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# EXERCISE -> Your life in Weeks
age = 24
max_age = 90

remaining_years = max_age - age

print(f"You have left {remaining_years * 365} days, {remaining_years * 52} weeks, {remaining_years * 12} months")