############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function() # The i doesn't reach 20, it stops at 19

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num]) # error happens when index is 6
                           # indexing starts at 0 and ends at 5

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.") # The code doesn't take into account the year 1994

# # Fix the Errors
# age = input("How old are you?") # -> add int(input(...))
# if age > 18: 
# print("You can drive at age {age}.") # -> add f string and fix indent on if

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # == is not =
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2 # only this line is indented in for
  b_list.append(new_item) # only puts the last element * 2 in the list
  print(b_list)

mutate([1,2,3,5,8,13])