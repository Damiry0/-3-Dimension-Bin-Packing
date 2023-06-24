from box_collision import box_collision
from box import Box


class Bin:
    _volume = 0

    def __init__(self, name, width, height, depth):
        self.name = name
        dims = [width, height, depth]
        dims.sort()
        self.width = dims[-1]
        self.height = dims[-2]
        self.depth = dims[-3]
        self.packed_items = []
        self.unpacked_items = []

    @property
    def volume(self) -> int:
        self._volume = self.width * self.depth * self.height
        return self._volume

    def print(self) -> str:
        return f'{self.name} width:{self.width} height:{self.height} depth:{self.depth} volume:{self.volume} ' \
               f'packed items volume:{self.packed_volume()} packed_volume:{100 - self.remaining_volume()}%'

    def remaining_volume(self):
        sum_vol = self.packed_volume()
        rem_vol = float(float(self.volume - sum_vol)/self.volume) * 100
        return rem_vol

    def packed_volume(self):
        sum_vol = 0
        for item in self.packed_items:
            sum_vol = sum_vol + item.volume
        return sum_vol

    def place_box_in_bin(self, box: Box, pivot) -> bool:
        can_pack = False
        temp_box_position = box.position
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
                box.position = temp_box_position

            return can_pack

        if not can_pack:
            box.position = temp_box_position

        return can_pack
