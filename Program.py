import random

number = random.randint(1, 10)
guess = 0
cond = True

while cond:
    guess = int(input("Guess a number from 1 - 10 range \n"))
    if guess > number:
        print("Its too high")
    elif guess < number:
        print("Its too low")
    else:
        print("Correct, you win")
        cond = False