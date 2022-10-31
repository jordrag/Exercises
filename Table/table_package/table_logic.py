# ********************************* Start of business logic *****************************************
class TableLogic(object):
    def __init__(self, template):
        self.template = template
        self.work_table_names = []
        self.work_table_prices = []
        self.designing_table()
        self.table_price()

    def designing_table(self):
        row_counter = 0             # Transforming user's table pattern to working matrix with instances
        try:
            for row in self.template:
                self.work_table_names.append([])
                for col in row:
                    temp_instance = col()
                    self.work_table_names[row_counter].append(temp_instance)
                row_counter += 1
        except Exception as err:
            raise TableError(err)

    def table_price(self):              # Calculating the table price
        total = 0

        for row in self.template:
            for col in row:
                price = col.price
                total += price
        return total


class TableError(Exception):            # Custom error class
    pass

# ********************************* End of business logic ******************************************
