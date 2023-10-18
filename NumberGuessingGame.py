
import random
from statistics import mean
from statistics import median
from statistics import mode

def start_game ():
    attempts = []
    while True:
        print ("Welcome to the number guessing game! Please choose a number between 1 and 100.")
        random_number = random.randint (1,100)
        game_attempts = 0
        while True:
            try:
                player_guess = input ("Enter your guess:   ")
                player_guess = int (player_guess)
                game_attempts +=1
                if player_guess > random_number:
                    print ("It's lower.")
                elif player_guess < random_number:
                    print ("It's higher.")
                else:
                    print ("Congrats, you guessed it!")
                    attempts.append(game_attempts)
                    break
            except ValueError:
                print("Please enter a number.")

#   5. Display the following data to the player
#     a. Display attempts it took them to get the correct number in this game
        print ("You needed {} attempts.".format (game_attempts))
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list

        play_again = input ("Do you want to play again? Y/N")
        if play_again.lower() == "y":
            random_number = random.randint (1,100)
            print ("Here we go. Let's see if you can beat your score")
        else:
            print ("OK. Bye!")
start_game()
