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


alum = Metal(10, "Aluminium")
cedar = Wood(5, "Cedar")
arm_glass = Glass(8, "Armored glass")

table = [[alum, alum, alum, alum, alum],
         [alum, cedar, arm_glass, cedar, alum],
         [alum, arm_glass, arm_glass, arm_glass, alum],
         [alum, cedar, arm_glass, cedar, alum],
         [alum, alum, alum, alum, alum]
         ]

table_width = len(table)
table_len = len(table[0])

for row in range(table_width):
    for col in range(table_len):
        print table[row][col]
        

# class PrintingTable(object):
#     def __init__(self):
#         table = TableDesign()
#         print table
#
#
#     for row in range(0, table_len):
#         table.append([])
#         for col in range(0, 10):
#             table[row].append("")
