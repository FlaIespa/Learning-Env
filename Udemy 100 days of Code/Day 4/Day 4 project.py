import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# rock wins against scissors
# scissors win againt paper
# paper wins against rock

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

if choice == "0":
  print(rock)
elif choice == "1":
  print(paper)
else:
  print(scissors)

possibilities = [0,1,2]
computer_choice = str(random.choice(possibilities))

print(f"Computer choses:{computer_choice}")

if choice == "0" and computer_choice == "0":
  print(rock,"It's a draw")
elif choice == "0" and computer_choice == "1":
  print(paper,"Sorry. You lost")
elif choice == "0" and computer_choice == "2":
  print(scissors, "Congratulations. You win!")
elif choice == "1" and computer_choice == "0":
  print(rock, "Congratulations. You win!")
elif choice == "1" and computer_choice == "1":
  print(paper, "It's a draw")
elif choice == "1" and computer_choice == "2":
  print(scissors, "Sorry. You lost")
elif choice == "2" and computer_choice == "0":
  print(rock,"Sorry. You lost")
elif choice == "2" and computer_choice == "1":
  print(paper,"Congratulations. You win!")
else:
  print(scissors, "It's a draw")
