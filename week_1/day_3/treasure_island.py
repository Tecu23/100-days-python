print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\" ").lower()

if direction == "left":
  lake = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. type \"swim\" to swim across. ").lower()

  if lake == "wait":
    color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()

    if color == "yellow":
      print("You found the treasure. You win!")
    elif color == "blue":
      print("You entered a room of beasts. Game Over!")
    else:
      print("Game Over!")
  else:
    print("Game Over!")
else:
  print("Game Over!")
