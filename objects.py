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


class Container(Box):
    def __init__(self, width: int, height: int, depth: int, *args, **kwargs) -> None:
        super().__init__(width, height, depth)
        self.packed = []
        self.remaining_volume = self.volume

    def calculate_remaining_volume(self) -> int:
        sum_box_volume = 0
        for box in self.packed:
            sum_box_volume += box.volume
        self.remaining_volume = self.volume - sum_box_volume
        return self.remaining_volume

    def add_box(self, box: Box) -> int:
        if box.volume > self.remaining_volume:
            print("Element too large to fit into box")
        else:
            self.packed.append(box)
            self.remaining_volume = self.calculate_remaining_volume()
        return self.remaining_volume

    def add_box_at_coordinates(self, box: Box,
                               pivot) -> int:  # Python doesn't support function overloading dogshit language
        raise NotImplementedError

    def check_coordinates_in_container(self, box: Box) -> bool:
        if box.coordinates["x"] < self.coordinates["x"] or box.coordinates["x"] + box.width > self.coordinates[
            "x"] + self.width:
            return False
        if box.coordinates["y"] < self.coordinates["y"] or box.coordinates["y"] + box.height > self.coordinates[
            "y"] + self.height:
            return False
        if box.coordinates["z"] < self.coordinates["z"] or box.coordinates["z"] + box.depth > self.coordinates[
            "z"] + self.depth:
            return False
        return True

    def check_fit_in_selected_position(self, box: Box, position) -> bool:
        raise NotImplementedError

    def check_fit_in_default_position(self, box: Box) -> bool:
        # Should check if box is able to fit in (0,0,0) coordinatess
        raise NotImplementedError

    def check_box_collision(self: Box, checked_box: Box) -> bool:
        if self.coordinates["x"] < checked_box.coordinates["x"] < checked_box.coordinates["x"] + checked_box.width:
            return False

        return True

    def assign_box_position(self):

        return


a_b = b_b = c_b = 1
a_c = b_c = c_c = 4

my_container = Container(a_c, b_c, c_c)
my_box = Box(a_b, b_b, c_b)
my_static_box = Box(a_b, b_b, c_b)

print("Box volume is ", my_box.volume)
print("Volume is ", my_container.volume)

print("Adding box")
my_container.add_box(my_box)

print("Remaining volume is ", my_container.remaining_volume)
print("List of packed boxes ", my_container.packed)

print("Adding box")
my_container.add_box(my_static_box)

print("Remaining volume is ", my_container.remaining_volume)
print("List of packed boxes ", my_container.packed)
