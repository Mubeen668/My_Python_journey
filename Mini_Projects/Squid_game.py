# simple SQUID game program (rock, paper, scissors game)

import random

choices = ("rock", "paper", "scissors")
computer = random.choice(choices)

print("Welcome to the Squid Game!")

while True:
    player = input("Enter your choice(rock,paper,scissors)?: ").lower()

    if player not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue


    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("it's a TIE!")
    elif player == "rock":
        if computer == "scissors":
            print("You win! Rock crushes scissors.")
        else:
            print("You lose! Paper covers rock.")
    elif player == "paper":
        if computer == "rock":
            print("You win! Paper covers rock.")
        else:
            print("You lose! Scissors cut paper.")
    elif player == "scissors":
        if computer == "paper":
            print("You win! Scissors cut paper.")
        else:
            print("You lose! Rock crushes scissors.")
    
    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing! Goodbye!")
        break

    
    



