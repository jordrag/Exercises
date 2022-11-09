from hangman_package.hangman_logic import *


# ************************************** User interface **************************************************

# User interface
class UserInput(object):
    print("Hello, let's play *** Hangman *** !")
    print()
    while True:
        try:
            username = str(input("Enter username: "))
            difficulty = str(input("Choose difficulty level (easy, medium, hard): "))
            category = str(input("Choose category of words (animals, cars, cities): "))
            player = HangmanOne(username, category, difficulty)
            player.gaming()
            break
        except Exception:
            print("Please enter a valid parameters !")

# *********************************************************************************************************
