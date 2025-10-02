import random

number = random.randint(1, 100)
attempts = 7
score = 0

print("I'm thinking of a number between 1 and 100.")
print(f"You have {attempts} attempts to guess it.")

while True:
    for i in range(attempts):
        guess = int(input(f"Attempt {i+1}: Take a guess: "))
        
        if guess < number:
            print("Higher!")
        elif guess > number:
            print("Lower!")
        else:
            print(f"Correct! You've guessed it in {i+1} attempts.")
            score = attempts - i
            break
    else:
        print(f"Sorry, you've used all {attempts} attempts. The number was {number}.")

    print(f"Your score: {score}")
