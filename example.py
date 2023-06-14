from packing_algorithm import Packer
from bin import Bin
from box import Box
# allowed_rots = [0, 1, 2, 3, 4, 5]

packer = Packer()

for i in range(10):
    packer.add_bin(Bin(f'20-standard [bin {i}]', 234, 240, 589))
# packer.add_bin(Bin('large-envelope', 15, 12, 5))

def generate_items(nb_of_S = 0, nb_of_m = 0, nb_of_L = 0, nb_of_XL = 0, nb_of_T8=0, nb_of_T10=0):
    index = 1
    for i in range(nb_of_S):
        packer.add_item(Box(f'50g [powder {index}]', 20, 11, 11))
        index += 1
    for i in range(nb_of_m):
        packer.add_item(Box(f'250g [powder {index}]', 30, 20, 25))
        index += 1
    for i in range(nb_of_L):
        packer.add_item(Box(f'250g [powder {index}]', 53, 23, 32))
        index += 1
    for i in range(nb_of_XL):
        packer.add_item(Box(f'250g [powder {index}]', 70, 32, 40))
        index += 1
    for i in range(nb_of_T8):
        packer.add_item(Box(f'250g [powder {index}]', 40, 6, 29))
        index += 1
    for i in range(nb_of_T10):
        packer.add_item(Box(f'250g [powder {index}]', 30, 60, 30))
        index += 1


generate_items(nb_of_50g=5,nb_of_250g=5)
packer.pack(distribute_items=True)

for b in packer.bins_to_pack:
    if len(b.packed_items)>0:
        print(":::::::::::", b.toString())

        print("FITTED ITEMS:")
        for item in b.packed_items:
            print("====> ", item.toString())

        print("UNFITTED ITEMS:")
        for item in b.unpacked_items:
            print("====> ", item.toString())

        print("***************************************************")
        print("***************************************************")