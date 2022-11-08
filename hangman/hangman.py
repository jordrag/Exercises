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

# ******************************** The Abstract class ********************************************************
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

    @abstractmethod
    def gaming(self):
        pass

    # @abstractmethod
    # def commands(self):
    #     pass


# ***************************************** The game logic ***************************************************

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
        self.trigger = False
        self.guessed_letters = []
        self.fail_count = 1

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
        empty_list = []
        rnd_number = random.randrange(0, len(self.game_list))
        the_word = self.game_list.pop(rnd_number)
        for lett in the_word:
            empty_list.append("_")
        return {"the_word": the_word, "user_word": empty_list, "words_list": self.game_list}

    # The core...................

    def gaming(self):
        print()
        print(f"Hello {self.username}, you have {self.hil_points} HIL points, let's play !")

        ScreenPrint(self.the_word).empty_word()

        # Commands through the game for exit, hints, whole word suggestion, etc..
        # 1. Hint, 2. Stop, 3. Word, 4. Show/hide guessed letters

        def commands(command):
            if command == 1:
                ind = self.user_word.index("_")
                self.user_word[ind] = self.the_word[ind]
                ScreenPrint(self.user_word).in_game_print()

            elif command == 2:
                ScreenPrint(self.username).change_params(self.hil_points)
                self.trigger = True

            elif command == 3:
                whole_word = input("Please, enter the whole word you think it is: ")
                if whole_word == self.the_word or whole_word == self.the_word.lower():
                    self.trigger = True
                    self.hil_points += 1
                    ScreenPrint(self.username).win_result(self.hil_points)
                else:
                    ScreenPrint(self.fail_count).hangman()

            elif command == 4:
                ScreenPrint(self.guessed_letters).guessed_letters()

            elif command == 5:
                if self.hil_points - 10 >= 0:
                    self.fail_count -= 1
                    print("Now you have one more try !")
                else:
                    print("You don't have enough HIL points !")

            # ops = {1: hint(),
            #        2: stop(),
            #        3: word(),
            #        4: letters()}

        while True:
            if self.trigger:
                break

            letter = input("Ask a letter from the word: ")
            guessed_right = 0

            try:
                if letter == "@":
                    command = int(input("Choose command (1. Hint, 2. Quit game/Change category/Change diff, "
                                        "3. Guess whole word, 4. Show/hide guessed letters, "
                                        "5. Exchange HIL points to 1 additional try --> "))
                    commands(command)
                else:
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
                            ScreenPrint(self.username).win_result(self.hil_points)
                    else:
                        ScreenPrint(self.fail_count).hangman()
                        self.fail_count += 1
                        if self.fail_count == len(self.the_word) + 1:
                            ScreenPrint(self.username).lost_result(self.hil_points, self.the_word)
                            break

            except Exception:
                print("Invalid input !!!")

        Database.usernames_list[self.username] = self.hil_points
        a = input("Do yoy wanna quit (y/n) ?")
        if a == "y":
            print("OK, your HIL points are saved, bye !")
        elif a == "n":
            new_category = ""
            new_diff = ""
            b = int(input ("1. Change level, 2. Change category: "))
            if b == 1:
                new_diff = str(input("Choose difficulty level (easy, medium, hard): "))
                new_category = self.category
            elif b == 2:
                new_category = str(input("Choose category of words (animals, cars, cities): "))
                new_diff = self.difficulty

            player = HangmanOne(self.username, new_category, new_diff)
            player.gaming()

# *************************************************************************************************************

# *********************************** Printing info on the screen  ********************************************
class ScreenPrint(object):
    def __init__(self, value):
        # self.points = points
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
        print(self.value)

    def win_result(self, points):
        print(f"{self.value}, you won !")
        print(f"Total HIL points: {points}")

    def lost_result(self, points, word):
        print(f"Game over! {self.value}, you've lost !")
        print(f"The word is -> {word}")
        print(f"Total HIL points: {points}")

    def change_params(self,points):
        print ("Leaving...")
        print(f"Total HIL points: {points}")


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
