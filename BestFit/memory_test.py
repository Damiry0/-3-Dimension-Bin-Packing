from packing_algorithm import Packer
from BestFit.bin import Bin
from BestFit.box import Box
import tracemalloc
import numpy as np
import matplotlib.pyplot as plt
import time

allowed_rots = [0, 1, 2, 3, 4, 5]
x = np.arange(10, 400 + 10, 10)
memory_usage = []
time_usage = []
for num_items in x:
    start = time.time()
    tracemalloc.start()
    packer_1 = Packer()

    for i in range(0, 20):
        packer_1.add_bin(Bin('Container', 10, 10, 10, allowed_rots))

    for i in range(0, num_items):
        packer_1.add_item(Box('Box', 3, 3, 3))

    packer_1.BestFitAlgorithm()
    memory_usage.append(max(tracemalloc.get_traced_memory()))

    print(max(tracemalloc.get_traced_memory()))
    del packer_1
    end = time.time()
    time_usage.append((end-start) * 10**3)
    tracemalloc.stop()


plt.plot(x, memory_usage)
plt.title("Memory Usage")
plt.xlabel("Number of items")
plt.ylabel("Memory Usage [KiB]")
plt.grid()
plt.show()

plt.plot(x, time_usage)
plt.title("Time Allocated for Operation")
plt.xlabel("Number of items")
plt.ylabel("Time Allocated for Operation [ms]")
plt.grid()
plt.show()


