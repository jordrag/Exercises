# coding=utf-8

from table_package.materials import *
from table_package.table_logic import *
from table_package.table_printer import *

# ************************************  User's table pattern definition ********************************************

user_pattern = [[Aluminium, Aluminium, Aluminium, Aluminium, Aluminium],
                [Aluminium, Beech, Glass, Beech, Aluminium],
                [Aluminium, Glass, Glass, Glass, Aluminium],
                [Aluminium, Beech, Glass, Beech, Aluminium],
                [Aluminium, Hole, Hole, Hole, Aluminium],
                [Aluminium, Aluminium, Aluminium, Aluminium, Aluminium]
                ]

# *************************************************************************************************

while True:
    try:            # Error protection beginning

        user_input = str(input("Въведи какво желаеш да се разпечата: "))

# *********************** Defining what to print **************************************************

        design = TableDesign(user_pattern)
        print_price = TableDesign.table_price(design)

        Printer(design.work_table_names).printing(user_input)
        
        print ("The total price of this table is: {0} lv.".format(print_price))

# ********************** Diff type of errors raise ************************************************

    except TableError:
        print("ERROR during table construction")

    except Exception :
        print ("This parameter is not supported !")

    else:
        break

# *************************************************************************************************
