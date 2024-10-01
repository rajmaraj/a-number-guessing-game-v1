"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

import random
import statistics

numbers = list(range(1,21))
#print(numbers)

guess_counter = []
high_score = None

def stats():
    if guess_counter:
        global high_score
        high_score = min(guess_counter)
        mean_attempts = statistics.mean(guess_counter)
        median_attempts = statistics.median(guess_counter)
        mode_attempts = statistics.mode(guess_counter)
        try:
            mode_attempts = statistics.mode(guess_counter)
        except statistics.StatisticsError:
            mode_attempts = "No Mode Attempts"
        print(f"Can you beat the high score of {high_score}?")
        print(f"Mean attempts {mean_attempts}")
        print(f"Median attempts {median_attempts}")
        print(f"Mode attempts {mode_attempts}")
    else:
        print("No high score yet.")

def start_game():
    global random_answer
    random_answer = random.choice(numbers)
    #print(random_answer)
    print("Hello, Welcome to the Number Guessing Game!")
    print("Guess a number from the list above.\n")
    guess = None
    attempts = 0
    while guess != random_answer:
        guess = int(input('Take a guess: '))
        attempts += 1
        if guess < random_answer:
            print("It's Higher! :( ")
        elif guess > random_answer:
            print("It's Lower :( ")
        else: 
            #guess != random_answer
            # Can I remove this line above because else statement assumes the answer is correct?
            print(f"Got It! in {attempts} trys")
            guess_counter.append(attempts)

def play_again():
    while True:
        play_again_prompt = input("Do you want to play again? Yes/No: ").lower()
        if play_again_prompt == "yes":
            start_game()
            stats()
        elif play_again_prompt == "no":
            print("Goodbye!")
            break
        else:
            print("error please enter yes/no.")






#print(guess_counter)

# :done: Import the random and statistics modules.
# :done: Create the start_game function.
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