"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import statistics

numbers = list(range(1,21))
print(numbers)

random_answer = random.choice(numbers)
#print(random_answer)

guess_counter = []
high_score = None

def start_game():
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
            guess != random_answer
            # Can I remove this line above because else statement assumes the answer is correct?
            print(f"Got It! in {attempts} trys")
            guess_counter.append(attempts)

def leader():
    high_score = min(guess_counter)
    print(f"Can you beat the high score of {high_score}?")


start_game()
leader()
#print(guess_counter)


#player_guess = int(input('Take a guess: '))
# Create the start_game function.
# Raj - Added numbers with range, had to increase by one to allow for 20 number and add as a list to show each number.
#def start_game(guess):
# Write your code inside this function.
#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
# Raj - Had to change from "randint()" to "choice()" because it was a list not a numerical list.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".
#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
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