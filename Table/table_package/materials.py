# coding=utf-8

# *********************************** Start of data layer **********************************
class Material(object):  # Common materials class
    name = ""
    price = 0
    strength = 0

    def __init__(self, color="Natural"):
        self.color = color

    def __str__(self):
        return self.name


class Linden(Material):  # Липа
    price = 50
    name = "Linden"


class Beech(Material):  # Бук
    price = 50
    name = "Beech"



class Aluminium(Material):  # Алуминий
    price = 60
    name = "Alum"



class Steel(Material):  # Стомана
    price = 80
    name = "Steel"


class Glass(Material):  # Стъкло
    price = 50
    name = "Glass"



class Hole(Material):  # An empty space option
    price = 10
    name = "    "


# ********************************* End of data layer ***********************************************
