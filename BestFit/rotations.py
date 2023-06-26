class Rotations:
    @staticmethod
    def change(x, y, z, num) -> list:
        if num == 0:
            return [x, y, z]
        elif num == 1:
            return [y, x, z]
        elif num == 2:
            return [y, z, x]
        elif num == 3:
            return [z, y, x]
        elif num == 4:
            return [z, x, y]
        elif num == 5:
            return [x, z, y]



