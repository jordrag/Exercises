# ********************************* Start of business logic *****************************************
class TableLogic(object):
    def __init__(self, template):
        self.template = template
        # self.__table = self.logic(template)

    @classmethod
    def from_list(cls, user_list):
        return cls.logic(user_list)

    @property
    def table(self):
        return self.logic(self.template)

    # @property
    # def table(self):
    #     return self.__table
    #
    # @table.setter
    # def table(self, value):
    #     self.__table = value

    @staticmethod
    # Transforming user's table pattern to working matrix with instances
    def logic(template):
        instance_matrix = []
        row_counter = 0
        try:
            for row in template:
                instance_matrix.append([])
                for col in row:
                    temp_instance = col()
                    instance_matrix[row_counter].append(temp_instance)
                row_counter += 1
            return instance_matrix
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


# Custom error class
class TableError(Exception):
    pass

# ********************************* End of business logic ******************************************
