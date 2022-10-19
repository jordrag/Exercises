class Material(object):

    def __init__(self, strength, kind):
        self.kind = kind
        self.strength = strength


class Wood(Material):

    def __init__(self):
        super(Wood, self).__init__(strength=10, kind="cedar")

    def __str__(self):
        return "W"


class Glass(Material):

    def __init__(self):
        super(Glass, self).__init__(strength=9, kind="Armored glass")

    def __str__(self):
        return "G"


class Metal(Material):

    def __init__(self):
        super(Metal, self).__init__(strength=15, kind="Aluminium")

    def __str__(self):
        return "M"


# class TableDesign(object):
#     def __init__(self, table_len, table_width):
#
#         self.table_width = table_width
#         self.table_len = table_len
#
#     table_len = int(input("Enter table length:"))
#     table_width = int(input("Enter table width:"))
#
#     table = []
#     for width in range(table_width+1):
#         table.append([])
#         for length in range(table_len):
#             wanted_material = str(input("Enter material: "))
#             if wanted_material == "wood":
#                 table[width].append(Wood)
#             elif wanted_material == "metal":
#                 table[width].append(Metal)
#             elif wanted_material == "glass":
#                 table[width].append(Glass)
#             else:
#                 raise ValueError ("Not supported material")



class Printing(object):
    metal = str(Metal())
    wood = str(Wood())
    glass = str(Glass())
    table_len = 10
    # table_width = 10

    print (metal * table_len)
    print (metal + (wood * (table_len - 2)) + metal)
    print (metal+wood * 3 + glass * 2 + wood * 3 + metal)
    print (metal+wood*2+glass*4+wood*2+metal)
    print (metal+wood*2+glass*4+wood*2+metal)
    print (metal + wood * 3 + glass * 2 + wood * 3 + metal)
    print (metal + (wood * (table_len - 2)) + metal)
    print (metal * table_len)
