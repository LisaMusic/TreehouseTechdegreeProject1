
import random
from statistics import mean
from statistics import median
from statistics import mode

def start_game ():
    attempts = []
    while True:
        print ("Welcome to the number guessing game! Please choose a number between 1 and 100.")
        random_number = random.randint (1,100)
        guess_attempts = 0
        while True:
            try:
                player_guess = input ("Enter your guess:   ")
                player_guess = int (player_guess)
                guess_attempts +=1
                if player_guess > random_number:
                    print ("It's lower.")
                elif player_guess < random_number:
                    print ("It's higher.")
                else:
                    print ("Congrats, you got it!")
                    attempts.append(guess_attempts)
                    break
            except ValueError:
                print("Please enter a number.")

        print ("You needed {} attempts.".format (guess_attempts))
        print ("Mean: {}".format (mean(attempts)))
        print ("Median: {}".format (median(attempts)))
        print ("Mode: {}".format (mode(attempts)))

        play_again = input ("Do you want to play again? Y/N")
        if play_again.lower() == "y":
            random_number = random.randint (1,100)
            print ("Here we go. Let's see if you can beat your score:{}".format(min(attempts)))
        else:
            print ("OK. Bye!")
start_game()
