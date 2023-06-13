from packing_algorithm import Packer
from bin import Bin
from box import Box
import time
# allowed_rots = [0, 1, 2, 3, 4, 5]

packer = Packer()

def generate_boxes(nb_of_S = 0, nb_of_M = 0, nb_of_L = 0, nb_of_XL = 0, nb_of_T8=0, nb_of_T10=0):
    index = 1
    for i in range(nb_of_S):
        packer.add_item(Box(f'S [box {index}]', 20, 11, 11))
        index += 1
    for i in range(nb_of_M):
        packer.add_item(Box(f'M [box {index}]', 30, 20, 25))
        index += 1
    for i in range(nb_of_L):
        packer.add_item(Box(f'L [box {index}]', 53, 23, 32))
        index += 1
    for i in range(nb_of_XL):
        packer.add_item(Box(f'XL [box {index}]', 70, 32, 40))
        index += 1
    for i in range(nb_of_T8):
        packer.add_item(Box(f'T8 [box {index}]', 40, 6, 29))
        index += 1
    for i in range(nb_of_T10):
        packer.add_item(Box(f'T10 [box {index}]', 30, 60, 30))
        index += 1


for i in range(10):
    packer.add_bin(Bin(f'20-standard [bin {i}]', 117, 120, 295))
# packer.add_bin(Bin('large-envelope', 15, 12, 5))

generate_boxes(nb_of_S = 50, nb_of_M = 50, nb_of_L = 50, nb_of_XL = 50, nb_of_T8=50, nb_of_T10=50)
start = time.time()
packer.pack(distribute_items=True,bigger_first= False)
end = time.time()
print(f'time to calculate: {end-start}s')

for b in packer.bins_to_pack:
    if len(b.packed_items)>0:
        print(":::::::::::", b.toString())
        print("***************************************************")