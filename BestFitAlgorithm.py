import objects


class BestFitAlgorithm:
    def __init__(self):
        self.packByWidth = False
        self.packByHeight = False

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

        #while len(not_packed) <= 0:

