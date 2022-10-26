# ********************************* Start of business logic *****************************************

from table_package.exceptions import *
class TableDesign(object):
    def __init__(self, user_table):
        self.table_for_design = user_table
        self.work_table_names = []
        self.work_table_prices = []
        self.table_width = len(self.table_for_design)
        self.table_len = len(self.table_for_design[0])
        self.designing_table()
        self.table_price()

    def designing_table(self):

        for row in range(self.table_width):
            self.work_table_names.append([])
            for col in range(self.table_len):
                temp_instance = self.table_for_design[row][col]()
                self.work_table_names[row].append(temp_instance)

    def table_price(self):
        total = 0

        for row in range(self.table_width):
            for col in range(self.table_len):
                temp_instance = self.work_table_names[row][col]
                price = temp_instance.price
                total += price
        return total


# ********************************* End of business logic *****************************************
