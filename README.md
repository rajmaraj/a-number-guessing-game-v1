TreeHouse Tech Degree: Project 1
    Hello

This program written in python and when run will prompt a user with a welcome message to the guessing game along with high score. From there it will ask the user to guess, if lower/higher the program will let the user know. The number must be in range or will let the user know. The user has unlimited guesses and the same guess can be made. If there is something other than a number then the program will throw a value error and prompt for a number. 

After the user guesses the number correctly, a message will pop up with how many guesses it took for that session and save the attempts to display as high score next go around. Then a stats message will calculate and print to show the mean/median/mode of the gathered attempts. 

Gather a random number via random module from a list
    random_answer = random.choice(numbers)

Attempts list
    guess_counter = []

High score
    high_score = min(guess_counter)

Stats function
    def stats():

Game function
    def start_game():

Try again variable 
    try_again = input('Play again? Yes/No:  ').strip().lower()

Loop program
    while True:
    start_game()
    stats()

Break loop if answers are no.