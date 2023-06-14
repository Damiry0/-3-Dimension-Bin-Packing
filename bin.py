from main import box_collision
from box import Box


class Bin:
    _volume = 0

    def __init__(self, name, width, height, depth):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.packed_items = []
        self.unpacked_items = []

    @property
    def volume(self) -> int:
        self._volume = self.width * self.depth * self.height
        return self._volume
    
    def used(self) -> float:
        sum = 0
        for item in self.packed_items:
            sum += item.width * item.height * item.depth
        return ((float(sum)/self.volume)*100)

    def toString(self) -> str:
        return f'{self.name} width:{self.width} height:{self.height} depth:{self.depth} volume:{self.volume} used: {round(self.used(),1)}%'

    def place_box_in_bin(self, box: Box, pivot) -> bool:
        can_pack = False
        valid_item_position = box.position
        box.position = pivot

        for rotation in range(0, 6):
            box.rotation_type = rotation
            dimension = box.get_packing_configuration()
            if (self.width < pivot[0] + dimension[0] or self.height < pivot[1] + dimension[1]
                    or self.depth < pivot[2] + dimension[2]):
                continue

            can_pack = True

            for packed_item in self.packed_items:
                if box_collision(packed_item, box):
                    can_pack = False
                    break

            if can_pack:
                self.packed_items.append(box)

            if not can_pack:
                box.position = valid_item_position

            return can_pack

        if not can_pack:
            box.position = valid_item_position

        return can_pack
