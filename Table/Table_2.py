# coding=utf-8
class Material(object):  # Common materials class

    def __init__(self, price, color):
        self.kind = color
        self.strength = price


class Linden(Material):  # Липа

    def __init__(self, price=50, color="Natural"):
        super(Linden, self).__init__(price, color)

    def __str__(self):
        return "Linden"


linden = Linden()


class Beech(Material):  # Бук

    def __init__(self, price=60, color="Natural"):
        super(Beech, self).__init__(price, color)

    def __str__(self):
        return "Beech"


beech = Beech()


class Aluminium(Material):  # Алуминий

    def __init__(self, price=55, color="Natural"):
        super(Aluminium, self).__init__(price, color)

    def __str__(self):
        return "Alum"


alumin = Aluminium()


class Steel(Material):  # Стомана

    def __init__(self, price=80, color="Natural"):
        super(Steel, self).__init__(price, color)

    def __str__(self):
        return "Steel"


steel = Steel()


class Glass(Material):  # Стомана

    def __init__(self, price=35, color="Mat"):
        super(Glass, self).__init__(price, color)

    def __str__(self):
        return "Glass"


glass = Glass()


class Hole(Material):  # An empty space option

    def __init__(self, price=0, color="None"):
        super(Hole, self).__init__(price, color)

    def __str__(self):
        return "    "


hole = Hole()


class Printer(object):  # Printing the ready table on the screen
    def __init__(self, table_for_print):
        self.table = table_for_print

    def printing(self):
        table_width = len(self.table)
        table_len = len(self.table[0])

        for item in self.table:
            print('\t'.join(map(str, item)))


# ************************************  User interface ********************************************

user_pattern = [[alumin, alumin, alumin, alumin, alumin],
                [alumin, beech, glass, beech, alumin],
                [alumin, glass, glass, glass, alumin],
                [alumin, beech, glass, beech, alumin],
                [alumin, hole, hole, hole, alumin],
                [alumin, alumin, alumin, alumin, alumin]
                ]

# *************************************************************************************************

Printer(user_pattern).printing()
