# Peak Filling Slice Push heuristic algorithm
# We assume that we can not rotate the boxes
# Algorithm steps:
# 1.Boxes are sorted in decreasing order by height, width, length.
# 2.We creating a slice of cointainer with the width of the first box.
# 3.Each new box create a sub-slice (above the block) where we trying to add new another box
# 4.After reaching top of the container, we are trying to fill the lower subslice


from container import Container
from box import Box
from csv import reader

def load_data():
    dataset = list()
    box_list = []
    with open('data.csv', 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
        #print(dataset)
    for row in dataset:
        for _ in range(len(row)):
            row[_] = int(float(row[_]))
        row.sort(reverse=True)
        box_list.append(Box(row[0], row[1], row[2]))
    return box_list

if __name__ == "__main__":
    block_list = load_data()
    print(block_list)

    container0 = Container(100,100,100)
    i=2
    if(container0.check_box_in_container_and_with_others(block_list[i])):
        print(container0.add_box_at_coordinates(block_list[i],{'x': 0, 'y': 0, 'z': 0}))