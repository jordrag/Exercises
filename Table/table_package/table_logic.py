# ********************************* Start of business logic *****************************************
class TableLogic(object):
    def __init__(self, template):
        self.template = template
        # self.from_list(template)

    @classmethod
    def from_list(cls, template):
        work_table_names = []
        row_counter = 0             # Transforming user's table pattern to working matrix with instances
        try:
            for row in template:
                work_table_names.append([])
                for col in row:
                    temp_instance = col()
                    work_table_names[row_counter].append(temp_instance)
                row_counter += 1
            return cls(work_table_names)
        except Exception as err:
            raise TableError(err)

    @property
    def price(cls):              # Calculating the table price
        total = 0

        for row in cls.template:
            for col in row:
                price = col.price
                total += price
        return total


class TableError(Exception):            # Custom error class
    pass

# ********************************* End of business logic ******************************************
