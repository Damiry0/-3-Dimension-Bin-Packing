from BestFit.bin import Bin


class Packer:
    def __init__(self):
        self.bins_to_pack = []
        self.toPack = []
        self.notPacked = []
        self.queued_items = 0

        self.bins_to_pack.sort(key=lambda bin: bin.volume)
        self.notPacked.sort(key=lambda box: box.volume)

    def add_bin(self, added_bin: Bin):
        return self.bins_to_pack.append(added_bin)

    def add_item(self, added_item):
        self.notPacked.append(added_item)
        self.queued_items = len(self.notPacked)
        return

    @staticmethod
    def compute_pivot(item, item_pivot: int):
        if item_pivot == 0:   # back lower right
            pivot = [item.position[0] + item.width, item.position[1], item.position[2]]
        elif item_pivot == 1:  # front lower left
            pivot = [item.position[0], item.position[1], item.position[2] + item.depth]
        elif item_pivot == 2:  # back upper left
            pivot = [item.position[0], item.position[1] + item.height, item.position[2]]
        return pivot

    def BestFitAlgorithm(self):
        first_run = True

        while not self.notPacked or first_run:
            if len(self.notPacked) == 0:
                return
            first_run = False
            for i in range(0, len(self.bins_to_pack)):
                self.toPack = self.notPacked
                self.notPacked = []
                if not self.bins_to_pack[i].packed_items:
                    if len(self.toPack) == 0:
                        return
                    response = self.bins_to_pack[i].place_box_in_bin(self.toPack[0], [0, 0, 0])

                    if not response:
                        self.bins_to_pack[i].unpacked_items.append(self.toPack[0])

                if len(self.toPack) == 1:
                    return

                for j in range(1, len(self.toPack)):
                    currentItem = self.toPack[j]
                    fitted = False

                    for p in range(0, 3):
                        k = 0
                        while k < len(self.bins_to_pack[i].packed_items) and not fitted:
                            binItem = self.bins_to_pack[i].packed_items[k]
                            pivot = self.compute_pivot(binItem, p)

                            if self.bins_to_pack[i].place_box_in_bin(currentItem, pivot):
                                fitted = True
                                k = k + 1
                                break
                            k = k + 1

                        if fitted:
                            break

                    if not fitted:
                        self.notPacked.append(currentItem)


    # @staticmethod
    # def pack_to_bin(bin_to_pack: Bin, box_to_pack: Box):
    #     fitted = False
    #
    #     if not bin_to_pack.packed_items:  # first item packing
    #         response = bin_to_pack.place_box_in_bin(box_to_pack, [0, 0, 0])
    #
    #         if not response:
    #             bin_to_pack.unpacked_items.append(box_to_pack)
    #         return
    #
    #     for axis in range(0, 3):  # <-- Number of pivots
    #         packed_items = bin_to_pack.packed_items
    #
    #         for packed_item in packed_items:
    #             pivot = [0, 0, 0]
    #             w, h, d = packed_item.get_packing_configuration()
    #             if axis == 0:
    #                 pivot = [
    #                     packed_item.position[0] + w,
    #                     packed_item.position[1],
    #                     packed_item.position[2]
    #                 ]
    #             elif axis == 1:
    #                 pivot = [
    #                     packed_item.position[0],
    #                     packed_item.position[1] + h,
    #                     packed_item.position[2]
    #                 ]
    #             elif axis == 2:
    #                 pivot = [
    #                     packed_item.position[0],
    #                     packed_item.position[1],
    #                     packed_item.position[2] + d
    #                 ]
    #
    #             if bin_to_pack.place_box_in_bin(box_to_pack, pivot):
    #                 fitted = True
    #                 break
    #
    #         if fitted:
    #             break
    #
    #     if not fitted:
    #         bin_to_pack.unpacked_items.append(box_to_pack)
    #
    # def pack1(self, bigger_first=False, distribute_items=False, ):
    #     self.bins_to_pack.sort(key=lambda bin: bin.volume, reverse=bigger_first)
    #     self.items_to_pack.sort(key=lambda box: box.volume, reverse=bigger_first)
    #
    #     for bin in self.bins_to_pack:
    #         for item in self.items_to_pack:
    #             self.pack_to_bin1(bin, item)
    #
    #         if distribute_items:
    #             for item in bin.packed_items:
    #                 self.items_to_pack.remove(item)
    #
    # @staticmethod
    # def pack_to_bin1(bin_to_pack: Bin, box_to_pack: Box):
    #     fitted = False
    #
    #     if not bin_to_pack.packed_items:  # first item packing
    #         response = bin_to_pack.place_box_in_bin(box_to_pack, [0, 0, 0])
    #
    #         if not response:
    #             bin_to_pack.unpacked_items.append(box_to_pack)
    #         return
    #
    #     for axis in range(0, 3):  # <-- Number of pivots
    #         packed_items = bin_to_pack.packed_items
    #
    #         for packed_item in packed_items:
    #             pivot = [0, 0, 0]
    #             w, h, d = packed_item.get_packing_configuration()
    #             if axis == 0:
    #                 pivot = [
    #                     packed_item.position[0] + w,
    #                     packed_item.position[1],
    #                     packed_item.position[2]
    #                 ]
    #             elif axis == 1:
    #                 pivot = [
    #                     packed_item.position[0],
    #                     packed_item.position[1] + h,
    #                     packed_item.position[2]
    #                 ]
    #             elif axis == 2:
    #                 pivot = [
    #                     packed_item.position[0],
    #                     packed_item.position[1],
    #                     packed_item.position[2] + d
    #                 ]
    #
    #             if bin_to_pack.place_box_in_bin(box_to_pack, pivot):
    #                 fitted = True
    #                 break
    #
    #         if fitted:
    #             break
    #
    #     if not fitted:
    #         bin_to_pack.unpacked_items.append(box_to_pack)
