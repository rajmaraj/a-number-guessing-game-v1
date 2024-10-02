
import random
import statistics

numbers = list(range(1,21))
guess_counter = []

def stats():
    if guess_counter:
        mean_attempts = statistics.mean(guess_counter)
        median_attempts = statistics.median(guess_counter)
        try:
            mode_attempts = statistics.mode(guess_counter)
        except statistics.StatisticsError:
            mode_attempts = "No mode (all values unique)"

        print(f"\nStats:")
        print(f"Mean: {mean_attempts}")
        print(f"Median: {median_attempts}")
        print(f"Mode: {mode_attempts}")
    else:
        print("No stats yet")

def start_game():
    print("Hello, Welcome to the Number Guessing Game!")
    print("Guess a number from 1 to 20\n")

    while True:
        random_answer = random.choice(numbers)
        attempts = 0
        user_guess = None

        while user_guess != random_answer:
            try:
                user_guess = int(input('Take a guess:  '))
            except ValueError:
                print('Error, enter valid number')
                continue

            attempts += 1

            if user_guess < random_answer:
                print("It's Higher. :( ")
            elif user_guess > random_answer:
                print("It's Lower. :( ")

        print(f"Got It! in {attempts} tries")
        guess_counter.append(attempts)

        try_again = input('Play again? Yes/No:  ').strip().lower()
        if try_again != 'yes':
            break

while True:
    start_game()
    stats()
    play_again = input("\nDo you want to reset and play again? Yes/No: ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break