WEEK 1: Python Basics
Class 1: Introduction to Python
●
●
●
●
●
Python setup and IDEs (PyCharm, VSCode, Jupyter Notebook)
Basic syntax, variables, and data types
Input/Output
Simple arithmetic and logical operations
Task: Write a Python script that takes user input to create a "Mad Libs" story.

Solutions :-
adjective1 = input("Enter an adjective : ")
noun1 = input("Enter an noun : ")
verb1 = input("Enter the verb (past tense) :") 
adjective2 = input ("Enter another adjective : ")
noun2 = input("Enter the noun : ")
verb2 = input("Enter the verb : ")
story = f"Once upon a time, there was a {adjective1} {noun1} who {verb1} all day long. One day, it found a {adjective2} {noun2} and decided to {verb2} with it. And they lived happily ever after."
print("Here's your Mad Libs story: ")
print(story)

Output:-
Enter an adjective : silly
Enter an noun : dog
Enter the verb (past tense) :jumped
Enter another adjective : green
Enter the noun : tree
Enter the verb : danced
Here's your Mad Libs story: 
Once upon a time, there was a silly dog who jumped all day long. One day, it found a green tree and decided to danced with it. And they lived happily ever after.
# ============================================================================================= #
=== Code Execution Successful ===
# ============================================================================================= #
Class 2: Control Flow
●
●
●
●
Conditional statements (if, else, elif)
Loops (for, while)
Break and continue statements
Task: Create a text-based number-guessing game with score tracking.

Solution :-

import random
def start_game():
    print("Welcome to the Gaming World !")
    print("Here you have 10 chance to guess the Number ")
    number_to_guess = random.randint(1,100)
    score = 0 
    attempt = 0
    while True:
        guess = input("Enter the number between 1 to 100 or ( If you type exit you can quiet the game) : ")
        if guess.lower() == 'exit':
            print("you are exited from the game")
            break
        if not guess.isdigit():
            print("you are entered incorrectly plz enter the number")
            continue
        guess = int(guess)
        attempt +=1
        if guess < number_to_guess:
            print("The number is too low ")
            continue
        elif guess > number_to_guess:
            print("The number is too high")
            continue
        else :
            print("You entered number is correct")
            score +=10
            print(f"you guessed the number in {attempt} attempt and your score is {score} ")
        repeat = input("Do you want to play Again ?  if  type yes it will continue and no it will be exited from the game : ")
        if repeat.lower() == 'yes':
            print("You entered yes for contuining the game")
            start_game()
            break
        elif repeat.lower() == 'no':
            print(f"You entered the no and exited from the game and your final score is {score}")
            break
start_game()

Output :-
Welcome to the Gaming World !
Here you have 10 chance to guess the Number 
Enter the number between 1 to 100 or ( If you type exit you can quiet the game) : 70
The number is too high
Enter the number between 1 to 100 or ( If you type exit you can quiet the game) : 65
The number is too high
Enter the number between 1 to 100 or ( If you type exit you can quiet the game) : 45
The number is too high
Enter the number between 1 to 100 or ( If you type exit you can quiet the game) : 25
The number is too high
Enter the number between 1 to 100 or ( If you type exit you can quiet the game) : 20
The number is too low 
Enter the number between 1 to 100 or ( If you type exit you can quiet the game) : 23
The number is too high
Enter the number between 1 to 100 or ( If you type exit you can quiet the game) : 22
The number is too high
Enter the number between 1 to 100 or ( If you type exit you can quiet the game) : 21
You entered number is correct
you guessed the number in 8 attempt and your score is 10 
Do you want to play Again ?  if  type yes it will continue and no it will be exited from the game : no
You entered the no and exited from the game and your final score is 10

# ============================================================================================= #
=== Code Execution Successful ===
# ============================================================================================= #

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
WEEK 2: Data Structures
Class 3: Lists, Tuples, and Sets
●
●
●
●
Creating, modifying, and accessing lists
Tuple immutability and use cases
Set operations and applications
Task: Implement a basic "to-do list" app using lists.

