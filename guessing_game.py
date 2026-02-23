import random

print("🎯 Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 10.")

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = input("Enter your guess (or type 'q' to quit): ")

    if guess.lower() == 'q':
        print("Game exited. The number was:", secret_number)
        break

    guess = int(guess)
    attempts += 1

    if guess == secret_number:
        print("🎉 Correct! You guessed it in", attempts, "attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")