
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

    def toString(self) -> str:
        return f'{self.name} width:{self.width} height:{self.height} depth:{self.depth} volume:{self.volume}'

    def get_packing_configuration(self) -> list:
        if self.rotation_type == 0:
            self._packing_configuration = [self.width, self.height, self.depth]
        elif self.rotation_type == 1:
            self._packing_configuration = [self.height, self.width, self.depth]
        elif self.rotation_type == 2:
            self._packing_configuration = [self.height, self.depth, self.width]
        elif self.rotation_type == 3:
            self._packing_configuration = [self.depth, self.height, self.width]
        elif self.rotation_type == 4:
            self._packing_configuration = [self.depth, self.width, self.height]
        elif self.rotation_type == 5:
            self._packing_configuration = [self.width, self.depth, self.height]
        else:
            self._packing_configuration = []

        return self._packing_configuration
