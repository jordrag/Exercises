# ********************************* Start of presentation layer ********************************************

class Printer(object):  # Printing the ready table on the screen
    def __init__(self, table_for_print, param_for_print=0):
        self.table = table_for_print
        self.param = param_for_print

    def printing(self, user_input):
        result = []

        for row in self.table:
            tmp = ""
            for col in row:
                tmp += str(getattr(col, user_input)) + " "
            result.append(tmp)
        for line in result:
            print (line)


# ********************************* End of presentation layer ********************************************
