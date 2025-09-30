import random

number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Take a guess: "))
    if guess < number:
        print("Higher!")
    elif guess > number:
        print("Lower!")
    else:
        print("Correct! You've guessed it.")
