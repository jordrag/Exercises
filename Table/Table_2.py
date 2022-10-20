# coding=utf-8
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


class Printer(object):  # Printing the ready table on the screen
    def __init__(self, table_for_print):
        self.table = table_for_print

    def printing(self):
        # table_width = len(self.table)
        # table_len = len(self.table[0])

        for item in self.table:
            print('\t'.join(map(str, item)))


class Calculator(object):

    def __init__(self, table_for_calc):
        self.table_for_calc = table_for_calc

    def calculating(self):
        table_width = len(self.table_for_calc)
        table_len = len(self.table_for_calc[0])
        total = 0

        for row in range(table_width):
            for col in range(table_len):
                temp_instance = self.table_for_calc[row][col]
                price = temp_instance.price
                total += price

        return total


alumin = Aluminium()
linden = Linden()
beech = Beech()
steel = Steel()
glass = Glass()
hole = Hole()

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

# Calculating the price

total_sum = Calculator(user_pattern).calculating()
print
print ("The total price of this table is: {0} lv.".format(total_sum))
