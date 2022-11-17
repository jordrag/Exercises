from hangman_package.hangman_screen_print_v2 import *
from hangman_package.hangman_logic_v2 import *

class InputData(object):
    """ The initial interface to take data from user and start the game:
        username -> the name of the player
        difficulty -> separated in 3 levels depending the word length,
        easy (3-5 symbols),
        medium (6-8),
        hard (9-30)
        category -> starting with 3 categories (cars, animals, cities)
        but could be extended during the time
    """

    visualisation = ScreenPrint

    user_data = visualisation.entering_game()
    username = user_data[0]
    difficulty = user_data[1]
    category = user_data[2]

run(InputData.username, InputData.difficulty, InputData.category)

# **************************************************************************************************

