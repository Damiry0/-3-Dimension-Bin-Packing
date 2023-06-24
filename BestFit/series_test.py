from BestFit.packing_algorithm import Packer
from BestFit.bin import Bin
from BestFit.box import Box
import random

allowed_rots = [0]
boxes_list = []
for i in range(0, 50):
    boxes_list.append(Box('50g [powder 1]', random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)))
print("################################################")
print("::::::::::: Allowed rotations : ", allowed_rots, ":::::::::::")
print("################################################")
packer_1 = Packer()
# Test series 1 - checking rotations

packer_1.add_bin(Bin('Container', 10, 10, 10))
packer_1.add_bin(Bin('Container', 10, 10, 10))
packer_1.add_bin(Bin('Container', 10, 10, 10))
packer_1.add_bin(Bin('Container', 10, 10, 10))

for i in range(0, 50):
    packer_1.add_item(boxes_list[i])

packer_2 = packer_1
# packer_1.pack1(distribute_items=True)
packer_1.BestFitAlgorithm()

for i in range(len(packer_1.bins_to_pack)):
    if len(packer_1.bins_to_pack[i].packed_items) != 0:
        print("::::::::::: Bin Num: ", i + 1)
        print(packer_1.bins_to_pack[i].print())
        print("Items packed: ", len(packer_1.bins_to_pack[i].packed_items))

# packer_2.BestFitAlgorithm()
#
# for i in range(len(packer_2.bins_to_pack)):
#     print("::::::::::: Bin Num: ", i + 1)
#     print(packer_2.bins_to_pack[i].toString())
#     print("Items packed: ", len(packer_2.bins_to_pack[i].packed_items))



# allowed_rots = [0, 2, 4]
# print("######################################################")
# print("::::::::::: Allowed rotations : ", allowed_rots, ":::::::::::")
# print("######################################################")
# packer_2 = Packer()
#
# packer_2.add_bin(Bin('Container', 10, 10, 10, allowed_rots))
# packer_2.add_bin(Bin('Container', 10, 10, 10, allowed_rots))
# packer_2.add_bin(Bin('Container', 10, 10, 10, allowed_rots))
# packer_2.add_bin(Bin('Container', 10, 10, 10, allowed_rots))
#
# for i in range(len(boxes_list)):
#     packer_2.add_item(boxes_list[i])
#
# packer_2.pack(distribute_items=True)
#
# for i in range(len(packer_2.bins_to_pack)):
#     print("::::::::::: Bin Num: ", i + 1)
#     print(packer_2.bins_to_pack[i].toString())
#     print("Items packed: ", len(packer_2.bins_to_pack[i].packed_items))
#
#
# allowed_rots = [0, 1, 2, 3, 4, 5]
# print("###############################################################")
# print("::::::::::: Allowed rotations : ", allowed_rots, ":::::::::::")
# print("###############################################################")
# packer_3 = Packer()
#
# packer_3.add_bin(Bin('Container', 10, 10, 10, allowed_rots))
# packer_3.add_bin(Bin('Container', 10, 10, 10, allowed_rots))
# packer_3.add_bin(Bin('Container', 10, 10, 10, allowed_rots))
# packer_3.add_bin(Bin('Container', 10, 10, 10, allowed_rots))
#
# for i in range(len(boxes_list)):
#     packer_3.add_item(boxes_list[i])
#
# packer_3.pack(distribute_items=True)
#
# for i in range(len(packer_3.bins_to_pack)):
#     print("::::::::::: Bin Num: ", i + 1)
#     print(packer_3.bins_to_pack[i].toString())
#     print("Items packed: ", len(packer_3.bins_to_pack[i].packed_items))


