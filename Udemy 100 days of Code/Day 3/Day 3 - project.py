print("Welcome to Treasure Island. Your mission is to find the treasure.")

direction = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'.")
if direction == "left":
  wait = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
  if wait == "wait":
    color = input("You arrive at the island unharmed. There is a house with 3 door. One red, one yellow, one blue. Which color do you choose?")
    if color == "red":
      print("Burned by fire. Game Over.")
    elif color == "blue":
      print("Eaten by beasts. Game Over.")
    elif color == "yellow":
      print("You win!")
    else:
      print("Game Over.")
  else:
   print("Attacked by a trout. Game Over.")   

else:
  print("Fall into a hole. Game over")