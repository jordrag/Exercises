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


class UsedMaterials(object):
    def __init__(self):
        self.mat_1 = Metal(10, "Aluminium")
        self.mat_2 = Wood(5, "Cedar")
        self.mat_3 = Glass(8, "Armored glass")


class TableDesign(object):
    def __init__(self):
        materials = UsedMaterials()

        self.table = [[materials.mat_1, materials.mat_1, materials.mat_1, materials.mat_1, materials.mat_1],
                      [materials.mat_1, materials.mat_2, materials.mat_3, materials.mat_2, materials.mat_1],
                      [materials.mat_1, materials.mat_3, materials.mat_3, materials.mat_3, materials.mat_1],
                      [materials.mat_1, materials.mat_2, materials.mat_3, materials.mat_2, materials.mat_1],
                      [materials.mat_1, materials.mat_1, materials.mat_1, materials.mat_1, materials.mat_1]
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
