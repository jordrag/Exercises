# coding=utf-8

# *********************************** Start of data layer **********************************
class Material(object):  # Common materials class
    name = ""
    price = 0
    strength = 0
    symbol = ""

    def __init__(self, color="Natural"):
        self.color = color

    def __str__(self):
        return self.name


class Linden(Material):  # Липа
    price = 50
    name = "Linden"
    symbol = "W"


class Beech(Material):  # Бук
    price = 50
    name = "Beech"
    symbol = "W"


class Aluminium(Material):  # Алуминий
    price = 60
    name = "Alum"
    symbol = "M"


class Steel(Material):  # Стомана
    price = 80
    name = "Steel"
    symbol = "M"


class Glass(Material):  # Стъкло
    price = 50
    name = "Glass"
    symbol = "G"


class Hole(Material):  # An empty space option
    price = 10
    name = "     "
    symbol = "H"


# ********************************* End of data layer ***********************************************
