# MODULE
import my_module
print(my_module.pi)

# RANDOM MODULE
import random

random_integer = random.randrange(1, 10)
random_float = random.random()
print(random_integer, random_float * 5)

love_score = random.randint(1, 100)
print(love_score)

# Exercise -> Heads or Tails
random_coin = random.randint(0, 1)

print(f"{'Heads' if random_coin == 0 else 'Tails'}")

# LISTS
fruits = ['item1', 'item2']

states_of_america = ['Delaware', 'Pennsylvania', '48 more']
states_of_america.append('California')
print(states_of_america[-1])

# Exercise -> Banker Roulette
names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

random_index = random.randint(0, len(names) - 1)
name_chosen = random.choice(names)
print(f"{names[random_index]} has to pay the bill.")

# IndexError -> print(names[100])

# Exercise -> Treasure Map
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]

col = 3
row = 1

map[row - 1][col - 1] = 'x'

print(f"{row1}\n{row2}\n{row3}")