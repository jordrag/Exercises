table = []

for row in range(0, 6):
    table.append([])
    for col in range(0, 10):
        table[row].append("")


class Cell:
    ALLOWED_MATERIALS = {"wood": "W", "metal": "M", "glass": "G"}

    def __init__(self, material, position_x, position_y):
        self.material = material
        self.position_x = int(position_x)
        self.position_y = int(position_y)

    @property
    def position_x(self):
        return self.position_x

    @position_x.setter
    def position_x(self, value):
        self.value = input("Enter position X:")
        if 0 < value < 9:
            position_x = int(value)
        raise ValueError("Position X must be in range 0-9 !")

    @property
    def position_y(self):
        return self.position_y

    @position_y.setter
    def position_y(self, value):
        self.value = input("Enter position Y:")
        if 0 < value < 5:
            position_y = int(value)
        raise ValueError("Position Y must be in range 0-5 !")

    @property
    def material(self):
        return self.material

    @material.setter
    def material(self, value):
        if value in self.ALLOWED_MATERIALS:
            material = self.ALLOWED_MATERIALS[value]
        raise ValueError("Material {mat} is not supported !".format(mat=value))


# cell_x = Cell.position_x
# cell_y = Cell.position_y
#
# table[cell_x][cell_y] = Cell.material
#
# for row in range(0,6):
#     print table[row]
