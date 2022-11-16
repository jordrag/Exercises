from abc import ABCMeta, abstractmethod
from six import with_metaclass

""" In this module is immplemented the whole visualisation of the game, no matter 
    of the print media:
    empty_word -> prints the entire empty word in the beggining of the game
    in_game_print -> prints the word during the game
    hangman -> prints the progress of wrong answers (hanging man)
    guessed_letters -> prints the all asked letters to this moment, on demand
    win_result -> used when the player guesses the word
    lost_result -> used when the player doesn't guess the word
    change_params -> used if user changes parameters of the game 
    """


# ******************************** The Abstract class **********************************************
class AbcPrint(with_metaclass(ABCMeta)):
    @abstractmethod
    def empty_word(self):
        pass

    @abstractmethod
    def in_game_print(self):
        pass

    @abstractmethod
    def hangman(self):
        pass

    @abstractmethod
    def guessed_letters(self):
        pass

    @abstractmethod
    def win_result(self):
        pass

    @abstractmethod
    def lost_result(self):
        pass

    @abstractmethod
    def change_params(self):
        pass


# *********************** Printing info on the screen in ASCII format  *****************************

class ScreenPrint(AbcPrint):
    def __init__(self, value):
        self.value = value

    def empty_word(self):
        print()
        for i in self.value:
            print(" _ ", end="")
        print()

    def in_game_print(self):
        print(" ".join(self.value))

    def hangman(self):
        print("It's wrong ! Hanging in progress...")
        print("*" * self.value)

    def guessed_letters(self):
        print(self.value)

    def win_result(self, hil_points, game_points):
        print(f"{self.value}, you won !")
        print(f"Total game points left: {game_points}")
        print(f"Total HIL points: {hil_points}")

    def lost_result(self, hil_points, word, game_points):
        print(f"Game over! {self.value}, you've lost !")
        print(f"The word is -> {word}")
        print(f"Total earned game points: {game_points}")
        print(f"Total HIL points: {hil_points}")

    def change_params(self,points):
        print ("Leaving...")
        print(f"Total HIL points: {points}")


# **************************************************************************************************
