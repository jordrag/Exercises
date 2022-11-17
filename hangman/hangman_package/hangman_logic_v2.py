import random
from abc import ABCMeta, abstractmethod
from six import with_metaclass
from hangman_package.hangman_db import *
from hangman_package.hangman_screen_print_v2 import *

class AbcHangman(with_metaclass(ABCMeta)):

    @abstractmethod
    def defining_game_list(self):
        pass

    @abstractmethod
    def extracting_hil_points(self):
        pass

    @abstractmethod
    def setting_start_data(self):
        pass

    @abstractmethod
    def gaming(self):
        pass


def run(username, difficulty, category):
    """ For starting the game """

    player = HangmanOne(username, difficulty, category)
    player.gaming()

class HangmanOne(AbcHangman):
    """
      The main logic of the game responsible for the gameplay:

      In the AbcHangman class main used variables are:
      self.exclude_list -> responsible to not repeat any word in the game
      self.usernames -> all usernames listed in the database
      self.username -> the current player name
      self.difficulty -> the chosen level to play
      self.category -> the chosen category to play
      self.game_list -> setting a list of words matching the player conditions
      self.hil_points -> player's hil_points taken from the database
      self.starting_data -> complete set of starting data for current game according defined
      conditions
      self.the_word -> the concrete word this game
      self.user_word -> first and empty word marked with dashes equivalent to the_word
      self.trigger -> a trigger for switching off the game
      self.guessed_letters -> list of asked letters during the game
      self.fail_count -> fail counter for each word
      self.game_points -> game points for each word, it begins with maximum number (the word length)
      self.visualisation -> variable where could be change printing interface

    """

    def __init__(self, name, diff, cat):
        self.exclude_list = Database.ex_word_read()
        self.usernames = Database.usernames_list
        self.username = name
        self.difficulty = diff
        self.category = cat
        self.game_list = self.defining_game_list()
        self.hil_points = self.extracting_hil_points()
        self.starting_data = self.setting_start_data()
        self.the_word = self.starting_data["the_word"]
        self.user_word = self.starting_data["user_word"]
        self.trigger = False
        self.guessed_letters = []
        self.fail_count = 0
        self.game_points = len(self.the_word)
        self.visualisation = ScreenPrint


    def defining_game_list(self):
        """ Setting a list of words matching the player conditions. """

        temp_list = []
        min_length = Database.levels[self.difficulty][0]
        max_length = Database.levels[self.difficulty][1]

        for word in Database.categories[self.category]:
            if min_length <= len(word) <= max_length and word not in self.exclude_list:
                temp_list.append(word)
        return temp_list


    def extracting_hil_points(self):
        """ Taking user's profile info from database,
        if it doesn't exist make new user with hil_points = 0. """

        if self.username not in Database.usernames_list:
            Database.usernames_list[self.username] = 0

        return Database.usernames_list[self.username]

    def setting_start_data(self):
        """ Complete set of starting data for current game according defined
      conditions. """

        empty_list = []
        rnd_number = random.randrange(0, len(self.game_list))
        the_word = self.game_list.pop(rnd_number)
        self.exclude_list.append(the_word)
        Database.exclude_word_save(self.exclude_list)
        for lett in the_word:
            empty_list.append("_")
        return {"the_word": the_word, "user_word": empty_list, "words_list": self.game_list}

    def check_letters(self, letter, guessed_right):
        """ The core of gamelogic, checks for accurate letter and manages win and lost result. """

        self.guessed_letters.append(letter)
        for i in range(len(self.the_word)):
            if self.the_word[i] == letter or self.the_word[i] == letter.lower() \
                    or self.the_word[i] == letter.upper():
                self.user_word[i] = self.the_word[i]
                guessed_right += 1

        if guessed_right != 0:
            self.visualisation(self.user_word).printing_in_game()
            if "_" not in self.user_word:
                self.trigger = True
                self.hil_points += 1
                self.visualisation(self.username).printing_win_result(self.hil_points,
                                                                      self.game_points)
        else:
            self.fail_count += 1
            self.game_points -= 1
            if self.game_points < 0:
                self.game_points = 0
            self.visualisation(self.fail_count).printing_hangman()
            if self.fail_count == len(self.the_word):
                self.visualisation(self.username).printing_lost_result(self.hil_points,
                                                                       self.the_word,
                                                                       self.game_points)
                self.trigger = True
        return self.trigger

    def saving_data(self):
        """ Saves user's score to the database. """

        self.usernames[self.username] = self.hil_points
        Database.users_save(self.usernames)

    def gaming(self):
        """ The gameplay, turns the game and tracks for letter or command. """

        self.visualisation.welcoming(self.username, self.hil_points)
        self.visualisation(self.the_word).printing_empty_word()

        while True:
            if self.trigger:
                break

            letter = self.visualisation.asking_letter(self.game_points)
            guessed_right = 0

            letter_check = self.visualisation.analysing_letter(letter)
            is_command = letter_check[0]
            command = letter_check[1]
            if is_command:
                Commands(self, command).manage_comms()
            else:
                self.check_letters(letter, guessed_right)
                if self.trigger:
                    break

       # Exit of game

        change_var = self.visualisation.changing_state()
        if change_var[0]:
            self.saving_data()
            Database.exclude_word_save(["blank"])

        # Make changes to the game

        else:
            self.saving_data()
            change_command = int(change_var[1])
            changes = self.visualisation.change_logic(change_command, self.difficulty, self.category)
            self.difficulty = changes[0]
            self.category = changes[1]
            run(self.username, self.difficulty, self.category)

class Commands(object):
    '''
    Commands through the game for exit, hints, whole word suggestion, etc..
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
        self.visualisation = ScreenPrint

    def giving_hint(self):
        """ Checks the possibility for hint letter and give it. """

        if self.player["game_points"] - 2 >= 0:
            self.player["game_points"] -= 2
            ind = self.user_word.index("_")
            self.user_word[ind] = self.the_word[ind]
            self.visualisation(self.user_word).printing_in_game()
        else:
            print("You haven't enough points for hint !")

    def stop_game(self):
        """ Stopping game. """

        self.player["trigger"] = True
        self.visualisation(self.username).leaving_game(self.player["hil_points"])

    def asking_whole_word(self):
        """ User tries to ask the whole word. """

        whole_word = input("Please, enter the whole word you think it is: ")
        if whole_word == self.the_word or whole_word == self.the_word.lower():
            self.player["trigger"] = True
            self.player["hil_points"] += 1
            self.visualisation(self.username).printing_win_result(self.player["hil_points"], self.player["game_points"])
        else:
            self.player["fail_count"] += 1
            self.visualisation(self.player["fail_count"]).printing_hangman()

    def printing_asked_letters(self):
        """ Represents all asked letters in this game to that moment. """

        self.visualisation(self.player["guessed_letters"]).presenting_asked_letters()

    def ask_additional_try(self):
        """ A possibility for one additional try after exchanging 10 HIL points. """

        if self.player["hil_points"] - 10 >= 0 and self.player["fail_count"] >= 1:
            self.player["fail_count"] -= 1
            self.player["hil_points"] -= 10
            print(f"Now you have one more try and {self.player['hil_points']} HIL points remaining !")
        else:
            print("You don't have enough HIL points !")

    def manage_comms(self):
        """ Method for handling commands:
            1. Hint
            2. Stop game
            3. Asking the whole word
            4. Printing the asked letters
            5. Additional try
        """

        ops = {1: self.giving_hint,
               2: self.stop_game,
               3: self.asking_whole_word,
               4: self.printing_asked_letters,
               5: self.ask_additional_try
               }

        func_name = ops[self.command].__name__
        func_obj = getattr(self, func_name)
        func_obj()

# **************************************************************************************************
