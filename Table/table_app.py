# coding=utf-8

from table_package.materials import *
from table_package.table_logic import *
from table_package.table_printer import *

# ************************************  User interface ********************************************

user_pattern = [[Aluminium, Aluminium, Aluminium, Aluminium, Aluminium],
                [Aluminium, Beech, Glass, Beech, Aluminium],
                [Aluminium, Glass, Glass, Glass, Aluminium],
                [Aluminium, Beech, Glass, Beech, Aluminium],
                [Aluminium, Hole, Hole, Hole, Aluminium],
                [Aluminium, Aluminium, Aluminium, Aluminium, Aluminium]
                ]

design = TableDesign(user_pattern)
print_price = TableDesign.table_price(design)

Printer(design.work_table_names).printing()
print

Printer(design.work_table_prices).printing()
print

print ("The total price of this table is: {0} lv.".format(print_price))

# *************************************************************************************************
