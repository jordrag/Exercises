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
    while True:
        username = str(input("Enter username: "))
        difficulty = str(input("Choose difficulty level (easy, medium, hard): "))
        category = str(input("Choose category of words (animals, cars, cities): "))
        player = StartingData(username, category, difficulty)


# Defining the exact word for this game
class WordMake(object):
    lett_list = []

    def __init__(self):
        self.game_list = UserInput.player.game_list

    @property
    def random_word(self):
        rnd_number = random.randrange(0,len(self.game_list))
        the_word = self.game_list.pop(rnd_number)
        return the_word

    def word_letters(self):
        for lett in self.random_word:
            self.lett_list.append(lett)





class Printer(object):
    print WordMake.random_word


class FinalResult(object):
    pass


class Commands(object):
    pass



