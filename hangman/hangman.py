username = str(input("Enter username: "))
difficulty = input("Choose difficulty level (1.Easy 2.Medium 3.Hard): ")
category = input("Choose category of words (1.Animals 2.Cars 3.Cities): ")


class UserData(object):
    usernames_list = {"Ace": 0,"Base": 0,"Case": 0}

    def __init__(self, name):
        self.username = name

        if self.username not in self.usernames_list:
            self.usernames_list[self.username] = 0

        HIL_points = self.usernames_list[self.username]


player_start_HIL = UserData(username)

class Category(object):
    animals = ["Cow","Elephant","Pinguin","Dog","Cat","Dragonfly"]
    cars = ["BMW","Ford","Toyota","Mazda","Maserati","Mercedes","Chevrolet","Lada"]
    cities = ["Varna","Bucurest","Mumbai","Moscow","Copenhagen","Sydney","Washington"]

class FinalResult(object):
    pass

class Commands(object):
    pass

