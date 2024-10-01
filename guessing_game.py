"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import statistics

print("Hello, Welcome to the Number Guessing Game!")
print("Guess a number from the list below\n")

numbers = list(range(1,21))
print(numbers)

random_answer = random.choice(numbers)
print(random_answer)

#guess = input("Please Guess The Number: ")?

def start_game(guess):
    if guess != random_answer:
        print("Wrong!")
    else:
        print("Correct!")

player_guess = int(input('Take a guess: '))

start_game(player_guess)

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