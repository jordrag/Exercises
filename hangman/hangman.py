username = str(input("Enter username: "))
difficulty = str(input("Choose difficulty level (easy, medium, hard): "))
category = str(input("Choose category of words (animals, cars, cities): "))


class UserData(object):
    usernames_list = {"Ace": 0,"Base": 0,"Case": 0}

    def __init__(self, name):
        self.username = name

    @property
    def hil_points(self):
        if self.username not in self.usernames_list:
            self.usernames_list[self.username] = 0

        return self.usernames_list[self.username]


class Category(object):
    animals = ["Cow","Elephant","Pinguin","Dog","Cat","Dragonfly"]
    cars = ["BMW","Ford","Toyota","Mazda","Maserati","Mercedes","Chevrolet","Lada"]
    cities = ["Varna","Bucurest","Mumbai","Moscow","Copenhagen","Sydney","Washington"]
    temp_list = []


    def __init__(self, category, difficulty):
        self.difficulty = difficulty
        self.category = category

        min_length = 0
        max_length = 0

        if self.difficulty == "easy":
            min_length = 3
            max_length = 5

        elif self.difficulty == "medium":
            min_length = 6
            max_length = 9

        elif self.difficulty == "hard":
            min_length = 9
            max_length = 30

        for a in category :
            if min_length <= len(a) <= max_length:
                self.temp_list.append(a)

class FinalResult(object):
    pass


class Commands(object):
    pass


player_hil_points = UserData(username).hil_points
words_list = Category(category,difficulty).temp_list
print words_list