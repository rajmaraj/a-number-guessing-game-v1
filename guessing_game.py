"""
DO NO USE
"""

import random
import statistics

numbers = list(range(1,21))
guess_counter = []

def stats():
    if guess_counter:# If guess counter has a value then run stats
        mean_attempts = statistics.mean(guess_counter)
        median_attempts = statistics.median(guess_counter)
        mode_attempts = statistics.mode(guess_counter)
    else:   
        print("Stats")
        print(f"Mean attempts {mean_attempts}")
        print(f"Median attempts {median_attempts}")
        print(f"Mode attempts {mode_attempts}")


def start_game():
    
    print("Hello, Welcome to the Number Guessing Game!")
    print("Guess a number from the list above.\n")
    
    while True:
        random_answer = random.choice(numbers)
        user_guess = None
        attempts = 0

        while user_guess != random_answer:
            try:
                user_guess = int(input('Take a guess: '))
            except ValueError:
                print('Error enter a number')
                continue

            attempts += 1

            if user_guess < random_answer:
                    print("It's Higher! :( ")
            elif user_guess > random_answer:
                    print("It's Lower :( ")
        else: 
            print(f"Got It! in {attempts} trys")
            guess_counter.append(attempts)
            
            try_again = input("Play again? Yes/No:  ").strip().lower()
            if try_again != 'yes':
                break


while True:
      start_game()
      stats()
      play_again = input('Play again? Yes/No:  ').strip().lower()
      if play_again != 'yes':
            print("Goodbye!")
            break

""" while True:
    start_game()
    stats()
    play_again = input("\nDo you want to reset and play again? Yes/No: ").strip().lower() # asks to play again and stores in play_again
    if play_again != 'yes': # if yes while true to run again
        print("Thanks for playing!")
        break # end program if no """

#player_guess = int(input('Take a guess: '))
# Create the start_game function.
# Raj - Added numbers with range, had to increase by one to allow for 20 number and add as a list to show each number.
#def start_game(guess):
# Write your code inside this function.
#   When the program starts, we want to:
#   ------------------------------------
#   :done: 1. Display an intro/welcome message to the player.
#   :done: 2. Store a random number as the answer/solution.
# Raj - Had to change from "randint()" to "choice()" because it was a list not a numerical list.
#   :done: 3. Continuously prompt the player for a guess.
#     :done: a. If the guess is greater than the solution, display to the player "It's lower".
#     :done: b. If the guess is less than the solution, display to the player "It's higher".
#   :done: 4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
#   :done: 5. Display the following data to the player
#    :done: a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.
# ( You can add more features/enhancements if you'd like to. )
# Kick off the program by calling the start_game function.