# **************** The database for users, categories and levels in the game *********************************
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

# ************************************************************************************************************