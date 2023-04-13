""" 
  LOOPS
"""

# For Loop
fruits = ['Apple', 'Peach', 'Pear']

for fruit in fruits:
  print(fruit)
  print(fruit + " Pie" )

# Exercise -> Average Height
student_heights = [180, 124, 165, 173, 189, 169, 146]

total_height = 0
number_of_students = 0

for height in student_heights:
  total_height += height
  number_of_students += 1

print(f"Average height of students {total_height//number_of_students}")

# Exercise -> High Score
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

max_score = float('-inf')

for score in student_scores:
  if score > max_score:
    max_score = score

print(f"The highest score is {max_score}")

# For loops and the range() function
total = 0
for number in range(101):
  total += number
print(total)

# Exercise -> Adding Even Numbers
total = 0
for number in range(101):
  if number % 2 == 0:
    total += number

total_2 = 0
for number in range(0, 101, 2):
  total_2 += number

print(f"Even number total is {total} or {total_2}")

# Exercise -> FizzBuzz

for number in range(1, 101):
  string = ""
  if number % 3 == 0:
    string += "Fizz"
  if number % 5 == 0:
    string += "Buzz"
  if number % 7 == 0:
    string += "Barr"

  print(f"{number} is {string}") 