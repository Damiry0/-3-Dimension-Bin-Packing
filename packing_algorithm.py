from box import Box
from bin import Bin


class Packer:
    def __init__(self):
        self.bins_to_pack = []
        self.items_to_pack = []
        self.unfit_items = []
        self.queued_items = 0

    def add_bin(self, added_bin: Bin):
        return self.bins_to_pack.append(added_bin)

    def add_item(self, added_item):
        self.items_to_pack.append(added_item)
        self.queued_items = len(self.items_to_pack)
        return

    @staticmethod
    def pack_to_bin(bin_to_pack: Bin, box_to_pack: Box):
        fitted = False

        if not bin_to_pack.packed_items:  # first item packing
            response = bin_to_pack.place_box_in_bin(box_to_pack, [0, 0, 0])

            if not response:
                    bin_to_pack.unpacked_items.append(box_to_pack)
            return

        for axis in range(0, 3):  # <-- Number of pivots
            packed_items = bin_to_pack.packed_items

            for packed_item in packed_items:
                pivot = [0, 0, 0]
                w, h, d = packed_item.get_packing_configuration()
                if axis == 0:
                    pivot = [
                        packed_item.position[0] + w,
                        packed_item.position[1],
                        packed_item.position[2]
                    ]
                elif axis == 1:
                    pivot = [
                        packed_item.position[0],
                        packed_item.position[1] + h,
                        packed_item.position[2]
                    ]
                elif axis == 2:
                    pivot = [
                        packed_item.position[0],
                        packed_item.position[1],
                        packed_item.position[2] + d
                    ]

                if bin_to_pack.place_box_in_bin(box_to_pack, pivot):
                    fitted = True
                    break

            if fitted:
                break

        if not fitted:
            bin_to_pack.unpacked_items.append(box_to_pack)

    def pack(self, bigger_first=False, distribute_items=False, ):
        self.bins_to_pack.sort(key=lambda bin: bin.volume, reverse=bigger_first)
        self.items_to_pack.sort(key=lambda box: box.volume, reverse=bigger_first)

        for bin in self.bins_to_pack:
            for item in self.items_to_pack:
                self.pack_to_bin(bin, item)

            if distribute_items:
                for item in bin.packed_items:
                    self.items_to_pack.remove(item)
