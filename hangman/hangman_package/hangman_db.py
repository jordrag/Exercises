# **************** The database for users, categories and levels in the game *********************************
class Database(object):
    usernames_list = {"Ace": 5, "Base": 10, "Case": 15}

    categories = {"animals": ["Cow", "Elephant", "Pinguin", "Dog", "Cat", "Dragonfly", "Butterfly", "Donkey", "Horse",
                              "Pig", "Tiger", "Lion", "Mouse", "Rat", "Cheetah", "Puma", "Aligator", "Crocodile"],
                  "cars": ["BMW", "Ford", "Toyota", "Mazda", "Maserati", "Mercedes", "Chevrolet", "Lada", "Moskvich",
                           "Volga", "Honda", "Suzuki", "Buick", "Opel", "Volkswagen", "Mercedes", "Lincoln",
                           "Holden", "Audi", "Volvo", "Subaru", "Peugeot", "Renault", "Citroen", "Ferrari",
                           "Lamborghini"],
                  "cities": ["Varna", "Bucurest", "Mumbai", "Moscow", "Copenhagen", "Sydney", "Washington", "Sofia",
                             "Burgas", "Stara Zagora", "Plovdiv", "London", "Toronto", "Ruse", "Veliko Tarnovo"]
                  }

    levels = {"easy": [3, 5], "medium": [6, 9], "hard": [9, 30]}

# ************************************************************************************************************
