# coding=utf-8
class Material(object):  # Common materials class

    def __init__(self, price, color):
        self.color = color
        self.price = price


class Linden(Material):  # Липа

    def __init__(self, price, color="Natural"):
        super(Linden, self).__init__(price, color)

    def __str__(self):
        return "Linden"


linden = Linden(price=50)


class Beech(Material):  # Бук

    def __init__(self, price, color="Natural"):
        super(Beech, self).__init__(price, color)

    def __str__(self):
        return "Beech"


beech = Beech(price=60)


class Aluminium(Material):  # Алуминий

    def __init__(self, price, color="Natural"):
        super(Aluminium, self).__init__(price, color)

    def __str__(self):
        return "Alum"


alumin = Aluminium(price=60)


class Steel(Material):  # Стомана

    def __init__(self, price, color="Natural"):
        super(Steel, self).__init__(price, color)

    def __str__(self):
        return "Steel"


steel = Steel(price=80)


class Glass(Material):  # Стъкло
    PRICE = 35
    COLOR = "Natural"

    def __init__(self, price, color="Natural"):
        super(Glass, self).__init__(price, color)

    def __str__(self):
        return "Glass"


glass = Glass(price=35)


class Hole(Material):  # An empty space option

    def __init__(self, price, color="None"):
        super(Hole, self).__init__(price, color)

    def __str__(self):
        return "    "


hole = Hole(price=10)


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