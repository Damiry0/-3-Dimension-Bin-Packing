from packing_algorithm import Packer
from BestFit.bin import Bin
from BestFit.box import Box
import random

if __name__ == '__main__':
    running = True
    print('This is the BestFitAlgorithm for the 3D Bin Packing Problem')
    while running:
        packer = Packer()
        print('Please input Container Parameter')
        print('Press enter to confirm choice, input integer values')
        a = False
        while a is not True:
            width = input('Width : ')
            try:
                assert type(int(width)) == int
                assert int(width) >= 1
                a = True
            except ValueError:
                print(f'Incorrect type: Container parameters should be of type "int" ')
                print(f'User input: {width}')
            except AssertionError:
                print(f'Incorrect value: Container width should be a positive integer ')
                print(f'User input: {width}')
        a = False
        while a is not True:
            height = input('Height : ')
            try:
                assert type(int(height)) == int
                assert int(height) >= 1
                a = True
            except ValueError:
                print(f'Incorrect type: Container parameters should be of type "int" ')
                print(f'User input: {height}')
            except AssertionError:
                print(f'Incorrect value: Container height should be a positive integer ')
                print(f'User input: {height}')
        a = False
        while a is not True:
            depth = input('Depth : ')
            try:
                assert type(int(depth)) == int
                assert int(depth) >= 1
                a = True
            except ValueError:
                print(f'Incorrect type: Container parameters should be of type "int" ')
                print(f'User input: {depth}')
            except AssertionError:
                print(f'Incorrect value: Container depth should be a positive integer ')
                print(f'User input: {depth}')

        print('Successfully inputted container parameters')
        packer.add_bin(Bin('Container', int(width), int(height), int(depth)))
        input("Press Enter to continue...")

        a = False
        while a is not True:
            box_num = input('Input number of boxes to pack : ')
            try:
                assert type(int(box_num)) == int
                assert int(box_num) >= 1
                a = True
            except ValueError:
                print(f'Incorrect type: Number of boxes parameter should be of type "int" ')
                print(f'User input: {box_num}')
            except AssertionError:
                print(f'Incorrect value: Number of boxes should be a positive integer ')
                print(f'User input: {box_num}')
        boxes_list = []
        print('Box parameters are generated randomly from a set of values defined by an upper and lower bound')
        a = False
        while a is not True:
            lower_bound = input('Input lower bound of box : ')
            try:
                assert type(int(lower_bound)) == int
                assert int(lower_bound) >= 1
                a = True
            except ValueError:
                print(f'Incorrect type: Number of boxes parameter should be of type "int" ')
                print(f'User input: {lower_bound}')
            except AssertionError:
                print(f'Incorrect value: Lower bound should be a positive integer ')
                print(f'User input: {lower_bound}')
        a = False
        while a is not True:
            higher_bound = input('Input higher bound of box : ')
            try:
                assert type(int(higher_bound)) == int
                assert int(higher_bound) > int(lower_bound)
                a = True
            except ValueError:
                print(f'Incorrect type: Number of boxes parameter should be of type "int" ')
                print(f'User input: {higher_bound}')
            except AssertionError:
                print(f'Incorrect value: Lower bound should be a positive integer and '
                      f'should be higher than the lower_bound: {lower_bound} ')
                print(f'User input: {higher_bound}')

        for i in range(0, int(box_num)):
            boxes_list.append(Box('Generic_Box', random.randint(int(lower_bound), int(higher_bound)),
                                  random.randint(int(lower_bound), int(higher_bound)),
                                  random.randint(int(lower_bound), int(higher_bound))))
        for i in range(0, int(box_num)):
            packer.add_item(boxes_list[i])
        print('Successfully inputted container parameters')
        input('Press enter to confirm and pack boxes into defined container...')
        packer.BestFitAlgorithm()
        if len(packer.bins_to_pack[0].packed_items) != 0:
            print('Boxes packed successfully!')
            print('Bin parameters:')
            print(f'Bin width: {width}')
            print(f'Bin height: {height}')
            print(f'Bin depth: {depth}')
            print("Container Volume: ", packer.bins_to_pack[0].volume)

            print("Number of items packed: ", len(packer.bins_to_pack[0].packed_items))
            print("Number of unpacked items: ", int(box_num) - len(packer.bins_to_pack[0].packed_items))
            print("Container packed volume: ", 100 - packer.bins_to_pack[0].remaining_volume(), "%")
            print("Item positions: ")
            for i in range(0, len(packer.bins_to_pack[0].packed_items)):
                print(f"Item {i}: ", packer.bins_to_pack[0].packed_items[i].print())
        else:
            print('No boxes could be packed')

        print("Operation finished successfully!")
        print("Do you want to run programme again?")
        a = False
        while a is not True:
            response = input('Y/N : ')
            if response == 'Y' or response == 'y':
                running = True
                a = True
                print('Rerunning...')
            elif response == 'N' or response == 'n':
                running = False
                a = True
                print('Ending programme...')
            else:
                print('Invalid input')




