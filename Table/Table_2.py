class Material(object):

    def __init__(self, strength, kind):
        self.kind = kind
        self.strength = strength


class Wood(Material):

    def __init__(self, strength=None, kind=None):
        super(Wood, self).__init__(strength, kind)

    def __str__(self):
        return "W"


class Glass(Material):

    def __init__(self, strength=None, kind=None):
        super(Glass, self).__init__(strength, kind)

    def __str__(self):
        return "G"


class Metal(Material):

    def __init__(self, strength=None, kind=None):
        super(Metal, self).__init__(strength, kind)

    def __str__(self):
        return "M"


class TableDesign(object):
    def __init__(self, table=None):

        alum = Metal(10, "Aluminium")
        cedar = Wood(5, "Cedar")
        arm_glass = Glass(8, "Armored glass")

        self.table = [[alum, alum, alum, alum, alum],
                 [alum, cedar, arm_glass, cedar, alum],
                 [alum, arm_glass, arm_glass, arm_glass, alum],
                 [alum, cedar, arm_glass, cedar, alum],
                 [alum, alum, alum, alum, alum]
                 ]

class Printer(object):
    def __init__(self, table_design):

        self.table = table_design.table

    def printing(self):

        table_width = len(self.table)
        table_len = len(self.table[0])

        for i in self.table:
            print('\t'.join(map(str, i)))

t = TableDesign()
p = Printer(t)
p.printing()
