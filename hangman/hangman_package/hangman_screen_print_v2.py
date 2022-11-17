from abc import ABCMeta, abstractmethod
from six import with_metaclass

""" In this module is immplemented the whole visualisation of the game, no matter 
    of the print media:
    entering_game -> start screen, welcomes and takes data from user
    welcoming -> giving info about starting HIL points
    printing_empty_word -> prints the entire empty word in the beggining of the game
    asking_letter -> asks for letter or command in the word
    analysing_letter -> make difference between letter and command
    changing_state -> purpose to quit or make changes in game parameters
    change_logic -> making changes in game parameters
    printing_in_game -> prints the word during the game
    printing_hangman -> prints the progress of wrong answers (hanging man)
    presenting_asked_letters -> prints the all asked letters to this moment, on demand
    printing_win_result -> used when the player guesses the word
    printing_lost_result -> used when the player doesn't guess the word
    leaving_game -> printing total HIL points at the end of the game 
    """


# ******************************** The Abstract class **********************************************
class AbcPrint(with_metaclass(ABCMeta)):
    @abstractmethod
    def printing_empty_word(self):
        pass

    @abstractmethod
    def printing_in_game(self):
        pass

    @abstractmethod
    def printing_hangman(self):
        pass

    @abstractmethod
    def presenting_asked_letters(self):
        pass

    @abstractmethod
    def printing_win_result(self):
        pass

    @abstractmethod
    def printing_lost_result(self):
        pass

    @abstractmethod
    def leaving_game(self):
        pass


# *********************** Printing info on the screen in ASCII format  *****************************

class ScreenPrint(AbcPrint):
    def __init__(self, value):
        self.value = value

    @staticmethod
    def entering_game():
        print("Hello, let's play *** Hangman *** !")
        print()

        # While loop for entering correct data from user

        while True:
            # try:
            username = str(input("Enter username: "))
            difficulty = str(input("Choose difficulty level (easy, medium, hard): "))
            category = str(input("Choose category of words (animals, cars, cities): "))
            return (username, difficulty, category)

        # except Exception:
        #     print("Please enter valid parameters !")

    @staticmethod
    def welcoming(username, hil_points):
        print()
        print(f"Hello {username}, you have {hil_points} HIL points, let's play !")

    def printing_empty_word(self):
        print()
        for i in self.value:
            print(" _ ", end="")
        print()

    @staticmethod
    def asking_letter(game_points):
        print(f"Game points: {game_points}")
        letter = input("Ask a letter from the word: ")
        return letter

    @staticmethod
    def analysing_letter(letter):
        is_command = False
        # try:
        if letter == "@":
            command = int(input("Choose command (1. Hint, "
                                "2. Quit game/Change category/Change diff, "
                                "3. Guess whole word, 4. Show/hide guessed letters, "
                                "5. Exchange HIL points to 1 additional try --> "))

            is_command = True
            return (is_command, command)

        else:
            return (is_command, None)
        # except Exception:
        #     print("Please choose only from the options above !!!")

    @staticmethod
    def changing_state():
        change_trigger = False
        while True:
            try:
                change = input("Do you wanna quit (y/n) ?")
                if change == "y":
                    change_trigger = True
                    print("OK, your HIL points are saved, bye !")
                    return (change_trigger, None)
                elif change == "n":
                    comm = int(input("1. Continue 2. Change level, 3. Change category: "))
                    return (change_trigger, comm)
            except Exception:
                print("Invalid input or empty category for this level, pls make another choice !")

    @staticmethod
    def change_logic(comm, level, categ):
        difficulty = level
        category = categ

        if comm == 1:
            pass
        elif comm == 2:
            difficulty = str(input("Choose difficulty level (easy, medium, hard): "))
        elif comm == 3:
            category = str(input("Choose category of words (animals, cars, cities): "))

        return (difficulty, category)


    def printing_in_game(self):
        print(" ".join(self.value))

    def printing_hangman(self):
        print("It's wrong ! Hanging in progress...")
        print("*" * self.value)

    def presenting_asked_letters(self):
        print(self.value)

    def printing_win_result(self, hil_points, game_points):
        print(f"{self.value}, you won !")
        print(f"Total game points left: {game_points}")
        print(f"Total HIL points: {hil_points}")

    def printing_lost_result(self, hil_points, word, game_points):
        print(f"Game over! {self.value}, you've lost !")
        print(f"The word is -> {word}")
        print(f"Total earned game points: {game_points}")
        print(f"Total HIL points: {hil_points}")

    def leaving_game(self, points):
        print ("Leaving...")
        print(f"Total HIL points: {points}")


# **************************************************************************************************
