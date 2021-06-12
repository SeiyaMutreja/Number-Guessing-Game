import random

number = random.randint(1, 9)

chances = 0

while(chances < 5):
    try:
        userAnswer = int(input("Guess A Number From 1 to 9 : "))
        if(userAnswer > 9 or userAnswer < 1):
            print("Try again")
    except:
        print("Better luck next time")

    if(userAnswer == number):
        print("Congratulations!! Your Guess Is Correct")
        chances = 6
    elif (userAnswer > number):
        print("Your Guess is Bigger than My number")
    elif (userAnswer < number):
        print("Your Guess is Smaller than My number")

    chances = chances + 1

if(chances == 5):
    print("Your have used all your chances")
    print('this is the number: {number} ')