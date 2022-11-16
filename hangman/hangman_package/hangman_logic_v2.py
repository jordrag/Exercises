import random
from abc import ABCMeta, abstractmethod
from six import with_metaclass
from hangman_package.hangman_db import *
from hangman_package.hagman_screen_print import *

""" The main logic of the game splitted in two main parts: 
    HangmanOne -> part of the main abstract class AbcHangman and responsible for the main gameplay
    Commands -> where the special commands are separated
    In the AbcHangman class main used variables are:
        self.exclude_list -> responsible to not repeat any word in the game
        self.usernames -> all usernames listed in the database
        self.username -> the current player name
        self.difficulty -> the chosen level to play
        self.category -> the chosen category to play
        self.game_list -> setting a list of words matching the player conditions
        self.hil_points -> player's hil_points taken from the database
        self.starting_data -> complete set of starting data for current game according previous 
        conditions
        self.the_word -> the concrete word this game
        self.user_word -> first and empty word marked with dashes equivalent to the_word
        self.trigger -> a trigger for switching off the game
        self.guessed_letters -> list of asked letters during the game
        self.fail_count -> fail counter for each word
        self.game_points -> game points for each word, it begins with maximum number (the word length)
    """

# ******************************** The Abstract class **********************************************
class AbcHangman(with_metaclass(ABCMeta)):

    @abstractmethod
    def game_list(self):
        pass

    @abstractmethod
    def hil_points(self):
        pass

    @abstractmethod
    def starting_data(self):
        pass

    @abstractmethod
    def gaming(self):
        pass


# ***************************************** The game logic *****************************************

class HangmanOne(AbcHangman):
    def __init__(self, name, cat, diff):
        self.exclude_list = Database.ex_word_read()
        self.usernames = Database.usernames_list
        self.username = name
        self.difficulty = diff
        self.category = cat
        self.game_list = self.game_list()
        self.hil_points = self.hil_points()
        self.starting_data = self.starting_data()
        self.the_word = self.starting_data["the_word"]
        self.user_word = self.starting_data["user_word"]
        self.trigger = False
        self.guessed_letters = []
        self.fail_count = 0
        self.game_points = len(self.the_word)

    # Making specific list according user's input data for category and difficulty level

    def game_list(self):
        temp_list = []
        min_length = Database.levels[self.difficulty][0]
        max_length = Database.levels[self.difficulty][1]

        for word in Database.categories[self.category]:
            if min_length <= len(word) <= max_length and word not in self.exclude_list:
                temp_list.append(word)
        return temp_list

    # Taking user's profile info from database, if it doesn't exist make new user with hil_points = 0

    def hil_points(self):
        if self.username not in Database.usernames_list:
            Database.usernames_list[self.username] = 0

        return Database.usernames_list[self.username]

    def starting_data(self):
        empty_list = []
        rnd_number = random.randrange(0, len(self.game_list))
        the_word = self.game_list.pop(rnd_number)
        self.exclude_list.append(the_word)
        Database.exclude_word_save(self.exclude_list)
        for lett in the_word:
            empty_list.append("_")
        return {"the_word": the_word, "user_word": empty_list, "words_list": self.game_list}


    # Checking the letters entered by the user

    def check_letters(self, letter, guessed_right):
        self.guessed_letters.append(letter)
        for i in range(len(self.the_word)):
            if self.the_word[i] == letter or self.the_word[i] == letter.lower() \
                    or self.the_word[i] == letter.upper():
                self.user_word[i] = self.the_word[i]
                guessed_right += 1

        if guessed_right != 0:
            ScreenPrint(self.user_word).in_game_print()
            if "_" not in self.user_word:
                self.trigger = True
                self.hil_points += 1
                ScreenPrint(self.username).win_result(self.hil_points, self.game_points)
        else:
            self.fail_count += 1
            self.game_points -= 1
            if self.game_points < 0:
                self.game_points = 0
            ScreenPrint(self.fail_count).hangman()
            if self.fail_count == len(self.the_word):
                ScreenPrint(self.username).lost_result(self.hil_points,
                                                       self.the_word, self.game_points)
                self.trigger = False
        return self.trigger

    # The gameplay itself

    def gaming(self):

        print()
        print(f"Hello {self.username}, you have {self.hil_points} HIL points, let's play !")

        ScreenPrint(self.the_word).empty_word()

        # Taking letters or commands from user

        while True:
            if self.trigger:
                break

            print(f"Game points: {self.game_points}")
            letter = input("Ask a letter from the word: ")
            guessed_right = 0

            try:
                if letter == "@":
                    command = int(input("Choose command (1. Hint, "
                                        "2. Quit game/Change category/Change diff, "
                                        "3. Guess whole word, 4. Show/hide guessed letters, "
                                        "5. Exchange HIL points to 1 additional try --> "))

                    Commands(self, command).manage_comms()

                else:
                    self.check_letters(letter, guessed_right)
                    if self.trigger:
                        break

            except Exception:
                print("Please choose only from the options above !!!")

        # Exit menu offering to quit or make some changes to the game

        while True:
            try:
                a = input("Do you wanna quit (y/n) ?")
                if a == "y":
                    self.usernames[self.username] = self.hil_points
                    Database.users_save(self.usernames)
                    Database.exclude_word_save(["blank"])
                    print("OK, your HIL points are saved, bye !")
                    break

                elif a == "n":
                    comm = int(input("1. Continue 2. Change level, 3. Change category: "))

                    def change_logic(comm):
                        def cont():
                            pass
                        def change_level():
                            self.difficulty = str(input("Choose difficulty level (easy, "
                                                        "medium, hard): "))

                        def change_category():
                            self.category = str(input("Choose category of words (animals, cars, "
                                                      "cities): "))

                        ops = {1: cont,
                               2: change_level,
                               3: change_category
                               }

                        return ops[comm]()

                    change_logic(comm)
                    self.usernames[self.username] = self.hil_points
                    Database.users_save(self.usernames)
                    player = HangmanOne(self.username, self.category, self.difficulty)
                    player.gaming()
                    break

            except Exception:
                print("Invalid input or empty category for this level, pls make another choice !")


# **************************** Special commands sector *********************************************

class Commands(object):
    ''' Commands through the game for exit, hints, whole word suggestion, etc..
                    1. Hint,
                    2. Quit game/Change category/Change diff,
                    3. Guess whole word,
                    4. Show/hide guessed letters,
                    5. Exchange HIL points to 1 additional try
            '''
    def __init__(self, player, command):

        self.player = player.__dict__
        self.command = int(command)
        self.the_word = self.player["the_word"]
        self.user_word = self.player["user_word"]
        self.username = self.player["username"]

    def hint(self):
        if self.player["game_points"] - 2 >= 0:
            self.player["game_points"] -= 2
            ind = self.user_word.index("_")
            self.user_word[ind] = self.the_word[ind]
            ScreenPrint(self.user_word).in_game_print()
        else:
            print("You haven't enough points for hint !")

    def stop(self):
        self.player["trigger"] = True
        ScreenPrint(self.username).change_params(self.player["hil_points"])

    def word(self):
        whole_word = input("Please, enter the whole word you think it is: ")
        if whole_word == self.the_word or whole_word == self.the_word.lower():
            self.player["trigger"] = True
            self.player["hil_points"] += 1
            ScreenPrint(self.username).win_result(self.player["hil_points"], self.player["game_points"])
        else:
            self.player["fail_count"] += 1
            ScreenPrint(self.player["fail_count"]).hangman()

    def letters(self):
        ScreenPrint(self.player["guessed_letters"]).guessed_letters()

    def additional_try(self):
        if self.player["hil_points"] - 10 >= 0 and self.player["fail_count"] >= 1:
            self.player["fail_count"] -= 1
            self.player["hil_points"] -= 10
            print(f"Now you have one more try and {self.player['hil_points']} HIL points remaining !")
        else:
            print("You don't have enough HIL points !")

    def manage_comms(self):
        ops = {1: self.hint,
               2: self.stop,
               3: self.word,
               4: self.letters,
               5: self.additional_try
               }

        func_name = ops[self.command].__name__
        func_obj = getattr(self, func_name)
        func_obj()

# **************************************************************************************************
