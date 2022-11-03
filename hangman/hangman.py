import random


# The database for users, categories and levels in the game
class Database(object):
    usernames_list = {"Ace": 5, "Base": 10, "Case": 15}

    categories = {"animals": ["Cow", "Elephant", "Pinguin", "Dog", "Cat", "Dragonfly"],
                  "cars": ["BMW", "Ford", "Toyota", "Mazda", "Maserati", "Mercedes", "Chevrolet", "Lada"],
                  "cities": ["Varna", "Bucurest", "Mumbai", "Moscow", "Copenhagen", "Sydney", "Washington"]
                  }

    levels = {"easy": [3, 5], "medium": [6, 9], "hard": [9, 30]}


# Taking specific data from database according to the user entry
class StartingData(object):
    def __init__(self, name, cat, diff):
        self.username = name
        self.difficulty = diff
        self.category = cat

    @property
    def game_list(self):
        temp_list = []
        min_length = Database.levels[self.difficulty][0]
        max_length = Database.levels[self.difficulty][1]

        for a in Database.categories[self.category]:
            if min_length <= len(a) <= max_length:
                temp_list.append(a)
        return temp_list

    @property
    def hil_points(self):
        if self.username not in Database.usernames_list:
            Database.usernames_list[self.username] = 0

        return Database.usernames_list[self.username]


# User interface
class UserInput(object):

    username = str(input("Enter username: "))
    difficulty = str(input("Choose difficulty level (easy, medium, hard): "))
    category = str(input("Choose category of words (animals, cars, cities): "))

    player = StartingData(username, category, difficulty)


# Defining the exact word for this game and some other words for the same level, if the player wants
class WordMake(object):
    def __init__(self, list):
        self.words_list = list

    @property
    def random_word(self):
        rnd_number = random.randrange(0, len(self.words_list))
        the_word = self.words_list.pop(rnd_number)
        return the_word

    @property
    def word_letters(self):
        letters_list = []
        for lett in self.random_word:
            letters_list.append(lett)
        return letters_list


# The game logic
class GamePlay:
    ''' Loop for the game
        Compare the user's letter to the letters from the word
        Tracing for user commands (stop game, whole word guess, hint)
        Calculating earned points
        Error checking
    '''


# Printing info on the screen (the bad and the good results)
class Printer(object):
    print WordMake(UserInput.player.game_list).random_word
    print WordMake(UserInput.player.game_list).word_letters

# Working on the final result, saving exit data to the database
class FinalResult(object):
    pass


# Commands through the game for exit, hints, whole word suggestion, etc..
class Commands(object):
    pass

