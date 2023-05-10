from itertools import permutations


class Box:
    def __init__(self, width: int, height: int, depth: int, *args, **kwargs) -> None:

        for obj in (width, height, depth):
            if type(obj) is not int:
                raise TypeError('Parameters should be of type int and is of type', type(obj))
            if obj <= 0:
                raise ValueError('Parameters should be greater than 0')

        self.width = width
        self.height = height
        self.depth = depth
        self.volume = width * height * depth
        self.coordinates = {'x': 0, 'y': 0, 'z': 0}
        self.default_coordinates = self.coordinates

    def assign_coordinates(self, x: int, y: int, z: int):
        self.coordinates["x"] = x
        self.coordinates["y"] = y
        self.coordinates["z"] = z
        return self.coordinates

    def rotate(self, configuration: int) -> None:
        try:
            perm = permutations([self.width, self.height, self.depth])
            self.assign_coordinates(perm[configuration])
        except ValueError:
            raise 'Cannot rotate object for selected configuration'
