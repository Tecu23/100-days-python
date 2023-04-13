import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if player_choice != 0 and player_choice != 1 and player_choice != 2:
  print("Wrong Choice!")

computer_choice = random.randint(0, 2)

print(f"You chose {'Rock' if player_choice == 0 else ('Paper' if player_choice == 1 else 'Scissors')} and the computer chose {'Rock' if computer_choice == 0 else ('Paper' if computer_choice == 1 else 'Scissors')}")

if player_choice == computer_choice:
  print("Draw")
else:
  if player_choice == 0:
    if computer_choice == 1:
      print("Lose")
    else:
      print("Win")
  elif player_choice == 1:
    if computer_choice == 2:
      print("Lose")
    else:
      print("Win")
  else:
    if computer_choice == 0:
      print("Lose")
    else:
      print("Win")



