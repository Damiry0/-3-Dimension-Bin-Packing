from rotations import Rotations


class Box:
    _volume = 0
    _packing_configuration = None

    def __init__(self, name, width, height, depth):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.rotation_type = 0
        self.position = [0, 0, 0]

    @property
    def volume(self) -> int:
        self._volume = self.width * self.depth * self.height
        return self._volume

    def print(self) -> str:
        return f'width:{self.width} height:{self.height} ' \
               f'depth:{self.depth} volume:{self.volume} position:{self.position}'

    def get_packing_configuration(self) -> list:
        self._packing_configuration = Rotations.change(self.width, self.height, self.depth, self.rotation_type)
        return self._packing_configuration
