import objects


# Dube, Erick, Leon R. Kanavathy, and Phoenix Woodview.
# "Optimizing three-dimensional bin packing through simulation."
# Sixth IASTED International Conference Modelling,
# Simulation, and Optimization. 2006.
class BestFitAlgorithm:
    def __init__(self):
        self.packByWidth = False
        self.packByHeight = False
        self.pivot = [0, 0, 0]

    def solve(self: objects.Container):
        if self.width < self.height & self.width < self.depth:
            self.packByWidth = True
            self.packByHeight = False
        if self.depth < self.height & self.depth < self.width:
            self.packByWidth = False
            self.packByHeight = False
        if self.height < self.depth & self.height < self.width:
            self.packByWidth = False
            self.packByHeight = True

        not_packed = self.packed  # funny

        while len(not_packed) <= 0:
            to_pack = not_packed
            not_packed = []
            new_container = objects.Container()
            if new_container.check_fit_in_default_position(to_pack[0]):
                for i in range(1, len(to_pack) - 1):
                    current_item = to_pack[i]
                    fitted = False
                    for p in range(0, 2):
                        k = 0
                        while k < len(new_container) & fitted == False:
                            bin_item = new_container[k]
                            if self.packByWidth:
                                self.pivot = p
                            elif self.packByHeight:
                                self.switch_pivot()
                            else:
                                self.switch_pivot()
                    if new_container.check_fit_in_selected_position(current_item, self.pivot):
                        new_container.add_box_at_coordinates(current_item, self.pivot)
                        fitted = True
                    else:
                        for j in range(0, 6):
                            # current_item.rotate()
                            if new_container.check_fit_in_selected_position(current_item, self.pivot):
                                new_container.add_box_at_coordinates(current_item, self.pivot)
                                fitted = True
                                break
                        # current_item.restore_default_position()
                        not_packed.append(current_item)

    def switch_pivot(self):  # todo arguments
        match self.pivot:
            case 0:
                NotImplemented
            case 1:
                NotImplemented
            case 2:
                NotImplemented
