from packing_algorithm import Packer
from bin import Bin
from box import Box
# allowed_rots = [0, 1, 2, 3, 4, 5]

packer = Packer()

packer.add_bin(Bin('small-envelope', 12, 6, 1))
packer.add_bin(Bin('large-envelope', 15, 12, 1))
packer.add_bin(Bin('small-box', 9, 5, 2))
packer.add_bin(Bin('medium-box', 11, 9, 6))
packer.add_bin(Bin('medium-2-box', 14, 12, 3))
packer.add_bin(Bin('large-box', 12, 12, 6))
packer.add_bin(Bin('large-2-box', 24, 12, 3))

packer.add_item(Box('50g [powder 1]', 4, 2, 2))
packer.add_item(Box('50g [powder 2]', 4, 2, 2))
packer.add_item(Box('50g [powder 3]', 4, 2, 2))
packer.add_item(Box('250g [powder 4]', 8, 4, 2))
packer.add_item(Box('250g [powder 5]', 8, 4, 2))
packer.add_item(Box('250g [powder 6]', 8, 4, 2))
packer.add_item(Box('250g [powder 7]', 8, 4, 2))
packer.add_item(Box('250g [powder 8]', 8, 4, 2))
packer.add_item(Box('250g [powder 9]', 8, 4, 2))

packer.pack()

for b in packer.bins_to_pack:
    print(":::::::::::", b.toString())

    print("FITTED ITEMS:")
    for item in b.packed_items:
        print("====> ", item.toString())

    print("UNFITTED ITEMS:")
    for item in b.unpacked_items:
        print("====> ", item.toString())

    print("***************************************************")
    print("***************************************************")