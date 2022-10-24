# ********************************* Start of presentation layer ********************************************

class Printer(object):  # Printing the ready table on the screen
    def __init__(self, table_for_print):
        self.table = table_for_print

    def printing(self):
        for item in self.table:
            print('\t'.join(map(str, item)))


# ********************************* End of presentation layer ********************************************
