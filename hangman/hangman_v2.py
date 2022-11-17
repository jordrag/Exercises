from hangman_package.hangman_screen_print_v2 import *
# from hangman_package.hangman_db import *
from hangman_package.hangman_logic_v2 import *

"""This is the main interface to communicate with the user when the game begins and when want 
    to change any parameter:
    username -> the name of the player
    difficulty -> separated in 3 levels depending the word length, easy (3-5 symbols), medium (6-8) 
    and hard (9-30)
    category -> starting with 3 categories but could be extended during the time 
    """

# User interface
class StartGame(object):

    user_data = ScreenPrint.entering_game()
    username = user_data[0]
    difficulty = user_data[1]
    category = user_data[2]

    @staticmethod
    def run(username, difficulty, category):
        player = HangmanOne(username, difficulty, category)
        player.gaming()


StartGame.run(StartGame.username, StartGame.difficulty, StartGame.category)

# **************************************************************************************************

