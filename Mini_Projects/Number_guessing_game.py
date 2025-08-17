# A simple number guessing game

import random

low =1
high = 69
answer = random.randint(low, high)
guesses = 0

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {low} and {high}.")

while True:
    guess = input("Make a guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    guesses += 1
    
    if guess < low or guess > high:
        print(f"Your guess is out of range! Please guess a number between {low} and {high}.")
    elif guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {answer} correctly!")
        break

print(f"number of guesses it took: {guesses}")