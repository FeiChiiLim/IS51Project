"""
This program lets user to guess the correct number from a randomly generated number between 1 to 100 from the program.
First, the program will randomly select a number from 1 through 100.
Set amount of guesses at 0.
Then it will allow user to input a number.
If the input number is smaller than the generated number, then print to user "Number too low. Guess again!"
If the input number is greater than the generated number, then print to user "Number too high. Guess again!"
If the user did not input a number, then print to user "You did not enter a number. Try again"
When the input number matches the randomly generated number, then print to user "Correct! You win!"
and print out the amount of guesses the user took the get the correct number.
"""


"""
import random
correctAnswer = random.randint(1,100)
gameOver = False
count = 0
"I've thought of a number from 1 through 100."

while gameOver is False:
    try:
        playerGuess = int(input("Guess the number: "))
    except ValueError:
        "You did not  enter a number. Try again."
    
    if playerGuess is correctAnswer:
        compareAnswer = "Correct"
    elif playerGuess greater than correctAnswer:
        compareAnswer = "Too High"
    elif playerGuess smaller than correctAnswer:
        compareAnswer = "Too Low"
    count +=1

    if compareAnswer is "Correct":
        "Correct! You win!", "You took", count, "guesses."
    elif compareAnswer is "Too High":
        "Number too high. Guess again!"
    else compareAnswer is "Too Low":
        "Number too low. Guess again!"
"""



import random
correctAnswer = random.randint(1,100)
gameOver = False
count = 0
print("I've thought of a number from 1 through 100.")

while gameOver == False:
    try:
        playerGuess = int(input("Guess the number: "))
    except ValueError:
        print("You did not enter a number. Try again.")
        continue
    
    if playerGuess == correctAnswer:
        compareAnswer = "Correct"
        gameOver = True
    elif playerGuess > correctAnswer:
        compareAnswer = "Too High"
    elif playerGuess < correctAnswer:
        compareAnswer = "Too Low"
    count +=1

    if compareAnswer == "Correct":
        print("Correct! You win!", "You took", count, "guesses.")
    elif compareAnswer == "Too High":
        print("Number too high. Guess again!")
    elif compareAnswer == "Too Low":
        print("Number too low. Guess again!")