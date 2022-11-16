from hangman_package.hangman_logic_v2 import *

"""This is the main interface to communicate with the user when the game begins and when want 
    to change any parameter:
    username -> the name of the player
    difficulty -> separated in 3 levels depending the word length, easy (3-5 symbols), medium (6-8) 
    and hard (9-30)
    category -> starting with 3 categories but could be extended during the time 
    """

# User interface
class UserInput(object):
    print("Hello, let's play *** Hangman *** !")
    print()

    # While loop for entering correct data from user

    while True:
        try:
            username = str(input("Enter username: "))
            difficulty = str(input("Choose difficulty level (easy, medium, hard): "))
            category = str(input("Choose category of words (animals, cars, cities): "))
            player = HangmanOne(username, category, difficulty)
            player.gaming()
            break
        except Exception:
            print("Please enter valid parameters !")

# **************************************************************************************************
