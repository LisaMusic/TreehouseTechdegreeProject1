
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
                if player_guess < 1 or player_guess >100:
                    raise ValueError
                
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
                print("Invalid input. Please enter a number between 1 and 100.")

        print (
            f"You needed {guess_attempts} attempts.\n"
            f"Mean: {mean(attempts)}\n"
            f"Median: {median(attempts)}\n"
            f"Mode: {mode(attempts)}"
        )

        while True:
            play_again = input ("Do you want to play again? Y/N")
            if play_again.lower() == "y":
                print (f"Here we go. Let's see if you can beat your score:{min(attempts)}")
                break
            elif play_again.lower()=="n":
                print ("OK. Bye!")
                return
            else:
                print ("Please enter 'Y' or 'N'.")

start_game()
