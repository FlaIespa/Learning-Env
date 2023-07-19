# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count = 0
true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

score = int(str(true)+str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
