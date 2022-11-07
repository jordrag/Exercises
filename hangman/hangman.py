import random
from abc import ABCMeta, abstractmethod
from six import with_metaclass


# **************** The database for users, categories and levels in the game **********************************
class Database(object):
    usernames_list = {"Ace": 5, "Base": 10, "Case": 15}

    categories = {"animals": ["Cow", "Elephant", "Pinguin", "Dog", "Cat", "Dragonfly"],
                  "cars": ["BMW", "Ford", "Toyota", "Mazda", "Maserati", "Mercedes", "Chevrolet", "Lada"],
                  "cities": ["Varna", "Bucurest", "Mumbai", "Moscow", "Copenhagen", "Sydney", "Washington"]
                  }

    levels = {"easy": [3, 5], "medium": [6, 9], "hard": [9, 30]}


# ************************************************************************************************************


# ***************************************** The game logic ***************************************************

class Hangman(with_metaclass(ABCMeta)):

    @abstractmethod
    def game_list(self):
        pass

    @abstractmethod
    def hil_points(self):
        pass

    @abstractmethod
    def starting_data(self):
        pass


class HangmanOne(Hangman):
    def __init__(self, name, cat, diff):
        self.username = name
        self.difficulty = diff
        self.category = cat
        self.game_list = self.game_list()
        self.hil_points = self.hil_points()
        self.starting_data = self.starting_data()
        self.the_word = self.starting_data["the_word"]
        self.user_word = self.starting_data["user_word"]

    # player = GamePlay(username, category, difficulty)

    # Making specific list according user's input data for category and difficulty level

    def game_list(self):
        temp_list = []
        min_length = Database.levels[self.difficulty][0]
        max_length = Database.levels[self.difficulty][1]

        for a in Database.categories[self.category]:
            if min_length <= len(a) <= max_length:
                temp_list.append(a)
        return temp_list

    # Taking user's profile info from database, if it doesn't exist make new user with hil_points = 0

    def hil_points(self):
        if self.username not in Database.usernames_list:
            Database.usernames_list[self.username] = 0

        return Database.usernames_list[self.username]

    def starting_data(self):
        letters_list = []
        rnd_number = random.randrange(0, len(self.game_list))
        the_word = self.game_list.pop(rnd_number)
        for lett in the_word:
            letters_list.append("_")
        return {"the_word": the_word, "user_word": letters_list, "words_list": self.game_list}

    def gaming(self):
        fail_count = 1

        Printer(self.the_word).empty_word()

        while True:
            letter = str(input("Ask a letter from the word: "))
            guessed_right = 0
            if letter == "/":
                command = input("Choose command (1.Hint, 2.Stop game, 3.If you wanna guess the whole word !")
                Commands(command)

            for i in range(len(self.the_word)):
                if self.the_word[i] == letter:
                    self.user_word[i] = letter
                    guessed_right += 1

            if guessed_right != 0:
                Printer(self.user_word).in_game_print()
                if "_" not in self.user_word:
                    Printer(self.username).win_result()
                    break
            else:
                Printer(fail_count).hangman()
                fail_count += 1
                if fail_count == len(self.the_word) + 1:
                    print("Game over! You lose!")
                    break


# Working with files, loading or saving data to the database
class FileOperations(object):

    def loading_data(self):
        pass

    def saving_data(self):
        pass


# Commands through the game for exit, hints, whole word suggestion, etc..
class Commands(object):
    def __init__(self, value):
        self.value = value

    def stop_game(self):
        pass

    def hint(self):
        pass

    def whole_word(self):
        pass


class UserOutput(object):
    pass


# *************************************************************************************************************

# ********************* Printing info on the screen (the bad and the good results) ****************************
class Printer(object):
    # print UserInput.player.username
    # print UserInput.player.hil_points
    # print WordMakeUp(UserInput.player.game_list).random_word

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
        print("*" * self.value)

    def guessed_letters(self):
        pass

    def not_guessed_letters(self):
        pass

    def win_result(self):
        print(f"{self.value}, you won !")

    def lost_result(self):
        print(f"Game over! {self.value}, you've lost !")


# ********************************************************************************************************


# ************************************** User interface **************************************************

# User interface
class UserInput(object):
    username = str(input("Enter username: "))
    difficulty = str(input("Choose difficulty level (easy, medium, hard): "))
    category = str(input("Choose category of words (animals, cars, cities): "))

    player = HangmanOne(username, category, difficulty)
    player.gaming()

# *********************************************************************************************************
