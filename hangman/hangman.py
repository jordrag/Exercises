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
class StartingDataFactory(object):
    def __init__(self, name, cat, diff):
        self.username = name
        self.difficulty = diff
        self.category = cat

    # Making specific list according user's input data for category and difficulty level
    @property
    def game_list(self):
        temp_list = []
        min_length = Database.levels[self.difficulty][0]
        max_length = Database.levels[self.difficulty][1]

        for a in Database.categories[self.category]:
            if min_length <= len(a) <= max_length:
                temp_list.append(a)
        return temp_list

    # Taking user's profile info from database, if it doesn't exist make new user with hil_points = 0
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

    player = StartingDataFactory(username, category, difficulty)


# Defining the exact word for this game and a new list of words for the same level, if the player wants
class WordMakeUp(object):
    def __init__(self, list):
        self.words_list = list

    @property
    def random_word(self):
        letters_list = []
        rnd_number = random.randrange(0, len(self.words_list))
        the_word = self.words_list.pop(rnd_number)
        for lett in the_word:
            letters_list.append(lett)
        return {"the_word": the_word, "letters": letters_list, "words_list": self.words_list}


# Printing info on the screen (the bad and the good results)
class Printer(object):
    # print UserInput.player.username
    # print UserInput.player.hil_points
    # print WordMakeUp(UserInput.player.game_list).random_word

    def __init__(self, value):
        self.value = value

    def empty_word(self):
        print
        for i in self.value:
            print(" _ "),
        print

    def in_game_print(self):
        print(" ".join(self.value))

    def hangman(self):
        print("*" * self.value)

    def guessed_letters(self):
        pass

    def not_guessed_letters(self):
        pass

    def result(self):
        pass


# The game logic
class GamePlay:
    ''' Loop for the game
        Compare the user's letter to the letters from the word
        Tracing for user commands (stop game, whole word guess, hint)
        Calculating earned points
        Error checking
    '''

    entry_data = WordMakeUp(UserInput.player.game_list).random_word
    points = 0
    game_word = []
    fail_count = 1
    entry_word = entry_data["the_word"]

    Printer(entry_data).empty_word()

    def gaming(self):
        while True:
            letter = str(input("Ask a letter from the word: "))
            guessed_right = 0
            for i in self.entry_word:
                if self.entry_word[i] == letter:
                    self.game_word[i] = letter
                    self.points += 1

            if self.points != 0:
                Printer(self.game_word).in_game_print()
                if "_" not in self.game_word:
                    print("You won!")
                    break
            # else:
            #     Printer(self.fail_count).hangman()
            #     self.fail_count += 1
            #     if self.fail_count == len():
            #         print("Game over! You lose!")
            #         break




# Working with files, loading or saving data to the database
class FileOperations(object):

    def loading_data(self):
        pass

    def saving_data(self):
        pass


# Commands through the game for exit, hints, whole word suggestion, etc..
class Commands(object):
    def stop_game(self):
        pass

    def hint(self):
        pass

    def whole_word(self):
        pass


