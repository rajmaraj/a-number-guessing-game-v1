
import random
import statistics

numbers = list(range(1,21))
guess_counter = []

def stats():
    if  len(guess_counter) > 0: # //if bool(guess_counter)// or //if guess_counter:// checks if guess counter has a value then run stats.
        mean_attempts = statistics.mean(guess_counter)
        median_attempts = statistics.median(guess_counter)
        try:
            mode_attempts = statistics.mode(guess_counter)
        except statistics.StatisticsError:
            mode_attempts = "No mode (all values unique)"

        print(f"\nStats:") # print stats of mean/median/mode statistics 
        print(f"Mean: {mean_attempts}")
        print(f"Median: {median_attempts}")
        print(f"Mode: {mode_attempts}")

def start_game():
    if len(guess_counter) > 0:
        high_score = min(guess_counter)
        print(f"\nHigh Score {high_score}")
    else:
        print("\nBe the first high score!")

    print("\nHello, Welcome to the Number Guessing Game!")
    print("Guess a number from 1 to 20\n")

    while True:
        random_answer = random.choice(numbers) # chooses random number from list
        attempts = 0
        user_guess = None

        while user_guess != random_answer:
            try:
                user_guess = int(input('\nTake a guess:  '))
                if not 1 <= user_guess <= 20: # limits user from using only 1-10 with //if not// print message
                    print('Must be a number between 1-20')
                    continue
            except ValueError: # shows error if not a number
                print('Error, enter valid number')
                continue

            attempts += 1

            if user_guess < random_answer:
                print("It's Higher. :( ")
            elif user_guess > random_answer:
                print("It's Lower. :( ")
        else: #can this else be removed? 
            print(f"\nGot It! in {attempts} tries")
            guess_counter.append(attempts)

            try_again = input('Play again? Yes/No:  \n').strip().lower() # asks to play again and stores in try_again
            if try_again != '8': # if yes while true and return to line 27
                break # if answer is no then stop game and run //stats// and play_again 

while True:
    start_game()
    stats()
