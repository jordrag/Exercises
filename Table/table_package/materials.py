# coding=utf-8

# *********************************** Start of data layer **********************************
class Material(object):  # Common materials class

    def __init__(self, price, color):
        self.color = color
        self.price = price


class Linden(Material):  # Липа
    PRICE = 50

    def __init__(self, price=PRICE, color="Natural"):
        super(Linden, self).__init__(price, color)

    def __str__(self):
        return "Linden"


class Beech(Material):  # Бук
    PRICE = 60

    def __init__(self, price=PRICE, color="Natural"):
        super(Beech, self).__init__(price, color)

    def __str__(self):
        return "Beech"


class Aluminium(Material):  # Алуминий
    PRICE = 60

    def __init__(self, price=PRICE, color="Natural"):
        super(Aluminium, self).__init__(price, color)

    def __str__(self):
        return "Alum"


class Steel(Material):  # Стомана
    PRICE = 80

    def __init__(self, price=PRICE, color="Natural"):
        super(Steel, self).__init__(price, color)

    def __str__(self):
        return "Steel"


class Glass(Material):  # Стъкло
    PRICE = 35
    COLOR = "Natural"

    def __init__(self, price=PRICE, color="Natural"):
        super(Glass, self).__init__(price, color)

    def __str__(self):
        return "Glass"


class Hole(Material):  # An empty space option
    PRICE = 10

    def __init__(self, price=PRICE, color="None"):
        super(Hole, self).__init__(price, color)

    def __str__(self):
        return "    "


# ********************************* End of data layer ***********************************************
