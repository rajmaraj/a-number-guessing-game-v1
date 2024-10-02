TreeHouse Tech Degree: Project 1
    Hello

This program written in python when run will prompt a user with a welcome message to the guessing game. From there it will ask the user to guess, if lower/higher the program will let the user know, the user has unlimited guesses and the same guess can be made. If there is something other than a number then the program will throw a value error and prompt for a number. 

After the user guesses the number correctly a message will pop up with how many guesses it took for that session and save the attempts. Then a stats message will calculate and print to show the mean/median/mode of the gathered attempts. 

Gather a random number via random module from a list
    random_answer = random.choice(numbers)

Attempts list
    guess_counter = []

Stats function
    def stats():

Game function
    def start_game():

Try again variable 
    try_again = input('Play again? Yes/No:  ').strip().lower()

Play again variable
    play_again = input("\nDo you want to reset and play again? Yes/No: ").strip().lower()

Break loop if answers are no.