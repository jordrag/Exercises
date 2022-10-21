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


class TableDesign(object):
    def __init__(self, user_table):
        self.table_for_design = user_table
        self.work_table = []
        self.table_width = len(self.work_table)
        self.table_len = len(self.work_table[0])
        self.designing_table()
        self.table_price()

    def designing_table(self):

        for row in range(self.table_width):
            self.work_table.append([])
            for col in range(self.table_len):
                temp_instance = self.table_for_design[row][col]()
                self.work_table[row].append(temp_instance)

    @property
    def table_price(self):
        return self.table_price

    @table_price.setter
    def table_price(self, value):
        total = 0

        for row in range(self.table_width):
            for col in range(self.table_len):
                temp_instance = self.work_table[row][col]
                price = temp_instance.price
                total += price


class Printer(object):  # Printing the ready table on the screen
    def __init__(self, table_for_print):
        self.table = table_for_print.work_table

    def printing(self):
        for item in self.table:
            print('\t'.join(map(str, item)))


# class Calculator(object):
#
#     def __init__(self, table_for_calc):
#         self.table_for_calc = table_for_calc
#         self.table_width = len(self.table_for_calc)
#         self.table_len = len(self.table_for_calc[0])
#         self.total_elements = self.table_width * self.table_len
#
#     def calculating_price(self):
#
#         total = 0
#
#         for row in range(self.table_width):
#             for col in range(self.table_len):
#                 temp_instance = self.table_for_calc[row][col]
#                 price = temp_instance.price
#                 total += price
#
#         return total


# ************************************  User interface ********************************************

user_pattern = [[Aluminium, Aluminium, Aluminium, Aluminium, Aluminium],
                [Aluminium, Beech, Glass, Beech, Aluminium],
                [Aluminium, Glass, Glass, Glass, Aluminium],
                [Aluminium, Beech, Glass, Beech, Aluminium],
                [Aluminium, Hole, Hole, Hole, Aluminium],
                [Aluminium, Aluminium, Aluminium, Aluminium, Aluminium]
                ]

# *************************************************************************************************


design = TableDesign(user_pattern)
price = TableDesign.table_price

Printer(design).printing()

# Calculating the price
#
# total_sum = Calculator(design.work_table).calculating_price()
# total_elements = Calculator(design.work_table).total_elements
print
print ("The total price of this table is: {0} lv.".format(price))

