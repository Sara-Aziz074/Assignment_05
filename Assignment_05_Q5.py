#Task : High Low

#We want you to gain more experience working with control flow and Booleans in Python. 
# To do this, we are going to have you develop a game! The game is called High-Low and
#  the way it's played goes as follows:

#1: Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and
#  one for a computer, who will be your opponent. You can see your number, but not 
# the computer's!

#2: You make a guess, saying your number is either higher than or lower than the computer's
#  number
#3: If your guess matches the truth (ex. you guess your number is higher, and then your
#  number is actually higher than the computer's), you get a point!
#4: These steps make up one round of the game. The game is over after all rounds have been
#  played.

import random


def high_low_game(rounds=5):
    print("Welcome to the High-Low Game!")
    print("-" * 32)
    
    score = 0  # Initialize the player's score

    for round_num in range(1, rounds + 1):
        # Generate a random number for the player and the computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"\nRound {round_num}")
        print(f"Your number is {player_number}")
        
        # Ask the player for their guess (higher or lower)
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        # Check if the player's guess was correct
        if (guess == "higher" and player_number > computer_number) or \
           (guess == "lower" and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Increase the score if the guess was correct
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        # Display the current score
        print(f"Your score is now {score}")

    # End of the game
    print("\nThanks for playing!")

# Run the game with a specified number of rounds
high_low_game(rounds=5)