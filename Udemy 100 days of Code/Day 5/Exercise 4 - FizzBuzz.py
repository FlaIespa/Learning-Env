#Write your code below this row 👇
for number in range(1,101):
    if number % 15 == 0:
        number = "FizzBuzz"
        print(number)
    elif number % 3 == 0:
        number = "Fizz"
        print(number)
    elif number % 5 == 0:
        number = "Buzz"
        print(number)
    else:
        print(number)
    
