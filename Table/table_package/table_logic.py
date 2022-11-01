# ********************************* Start of business logic *****************************************
class TableLogic(object):
    def __init__(self, template):
        self.template = template

    @classmethod
    # Transforming user's table pattern to working matrix with instances
    def from_list(cls, template):
        instance_matrix = []
        row_counter = 0
        try:
            for row in template:
                instance_matrix.append([])
                for col in row:
                    temp_instance = col()
                    instance_matrix[row_counter].append(temp_instance)
                row_counter += 1
            return cls(instance_matrix)
        except Exception as err:
            raise TableError(err)

    @property
    # Calculating the table price
    def price(self):
        total = 0
        for row in self.template:
            for col in row:
                price = col.price
                total += price
        return total


class TableError(Exception):
    # Custom error class
    pass

# ********************************* End of business logic ******************************************
