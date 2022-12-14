# **************** The database for users, categories and levels in the game ***********************
import json


class Database(object):
    # users = {"Ace": 5, "Base": 10, "Case": 15}
    # with open("hangman_package/usernames.json", "w") as write_users:
    #     json.dump(users, write_users)

    with open("hangman_package/usernames.json", "r") as read_users:
        usernames_list = json.load(read_users)

    with open("hangman_package/levels.json", "r") as read_levels:
        levels = json.load(read_levels)

    with open("hangman_package/categories.json", "r") as read_cats:
        categories = json.load(read_cats)

    @classmethod
    def users_save(cls, users):
        with open("hangman_package/usernames.json", "w") as write_users:
            json.dump(users, write_users)

    @classmethod
    def exclude_word_save(cls, ex_word):
        with open("hangman_package/exclude_word.json", "w") as write_ex_word:
            json.dump(ex_word, write_ex_word)

    @classmethod
    def ex_word_read(cls):
        with open("hangman_package/exclude_word.json", "r") as read_ex_word:
            exclude_list = json.load(read_ex_word)
        return exclude_list

# *************************************************************************************************
