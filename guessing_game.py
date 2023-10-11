"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import statistics

# Create the start_game function.
def start_game ():
# Write your code inside this function.
#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
    print ("Welcome to the number guessing game! Please choose a number between 1 and 100.")
#   2. Store a random number as the answer/solution.
    random_number = random.randint (1,100)
#   3. Continuously prompt the player for a guess.
    while True:
        try:
            player_guess = input ("Enter your guess:   ")
            player_guess = int (player_guess)
#     a. If the guess is greater than the solution, display to the player "It's lower".
            if player_guess > random_number:
                print ("It's lower.")
#     b. If the guess is less than the solution, display to the player "It's higher".
            elif player_guess < random_number:
                print ("It's higher.")
#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
            else:
                print ("Congrats, you guessed it!")
        except ValueError:
            print("Please enter a number.")
            
#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )
# Kick off the program by calling the start_game function.
