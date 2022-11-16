# ********************************* Start of presentation layer ********************************************
class TablePrinter(object):
    # Printing the ready table on the screen
    def __init__(self, table_for_print, param_for_print=0):
        self.table = table_for_print
        self.param = param_for_print # Parameter set by the user

    def printing(self, user_input):
        result = []             # Temporary matrix

        # Module for reading data and collecting it in new matrix for print
        for row in self.table:
            tmp = ""
            for col in row:
                tmp += str(getattr(col, user_input)) + " "
            result.append(tmp)

        # Printing the new matrix with data collected in it
        for line in result:
            print (line)
        print()

# ********************************* End of presentation layer *********************************************
