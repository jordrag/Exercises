# ********************************* Start of business logic *****************************************
class TableDesign(object):
    def __init__(self, user_table):
        self.table_for_design = user_table
        self.work_table_names = []
        self.work_table_prices = []
        self.table_width = len(self.table_for_design)
        self.table_len = len(self.table_for_design[0])
        self.designing_table()
        self.table_price()

    def designing_table(self):          # Transforming user's table pattern to working matrix with instances
        try:
            for row in range(self.table_width):
                self.work_table_names.append([])
                for col in range(self.table_len):
                    temp_instance = self.table_for_design[row][col]()
                    self.work_table_names[row].append(temp_instance)

        except Exception as err:
            raise TableError(err)

    def table_price(self):              # Calculating the table price
        total = 0

        for row in range(self.table_width):
            for col in range(self.table_len):
                temp_instance = self.work_table_names[row][col]
                price = temp_instance.price
                total += price
        return total


class TableError(Exception):            # Custom error class
    pass

# ********************************* End of business logic ******************************************
