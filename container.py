from box import Box


class Container(Box):
    def __init__(self, width: int, height: int, depth: int, *args, **kwargs) -> None:
        super().__init__(width, height, depth)
        self.packed = []
        self.remaining_volume = self.volume

    def calculate_remaining_volume(self) -> int:
        sum_box_volume = 0
        for box in self.packed:
            sum_box_volume += box.volume
        self.remaining_volume = self.volume - sum_box_volume
        return self.remaining_volume

    def add_box(self, box: Box) -> int:
        if box.volume > self.remaining_volume:
            print("Element too large to fit into box")
        else:
            self.packed.append(box)
            self.remaining_volume = self.calculate_remaining_volume()
        return self.remaining_volume
    

    def check_coordinates_in_container(self, box: Box) -> bool:
        if box.coordinates["x"] < self.coordinates["x"] or box.coordinates["x"] + box.width > self.coordinates[
            "x"] + self.width:
            return False
        if box.coordinates["y"] < self.coordinates["y"] or box.coordinates["y"] + box.height > self.coordinates[
            "y"] + self.height:
            return False
        if box.coordinates["z"] < self.coordinates["z"] or box.coordinates["z"] + box.depth > self.coordinates[
            "z"] + self.depth:
            return False
        return True
    
    def check_box_to_box(self, packed_box: Box, new_box: Box) -> bool:
        #x axis 
        if new_box.coordinates["x"] < packed_box.coordinates["x"]:
            if new_box.coordinates["x"] + new_box.width > packed_box.coordinates["x"]:
                return False
        if new_box.coordinates["x"] > packed_box.coordinates["x"]:
            if new_box.coordinates["x"] < packed_box.coordinates["x"] + packed_box.width:
                return False
        #y axis
        if new_box.coordinates["y"] < packed_box.coordinates["y"]:
            if new_box.coordinates["y"] + new_box.height > packed_box.coordinates["y"]:
                return False
        if new_box.coordinates["y"] > packed_box.coordinates["y"]:
            if new_box.coordinates["y"] < packed_box.coordinates["y"] + packed_box.height:
                return False
        #z axis
        if new_box.coordinates["z"] < packed_box.coordinates["z"]:
            if new_box.coordinates["z"] + new_box.depth > packed_box.coordinates["z"]:
                return False
        if new_box.coordinates["z"] > packed_box.coordinates["z"]:
          if new_box.coordinates["z"] < packed_box.coordinates["z"] + packed_box.depth:
                return False
        #the same coordinates:
        if new_box.coordinates == packed_box.coordinates:
            return False
        return True

    def check_fit_with_others_boxes(self, box: Box) -> bool:
        for packed_box in self.packed:
            #print(packed_box)
            if not self.check_box_to_box(packed_box, box):
                return False
        return True
    
    def check_box_in_container_and_with_others(self, box: Box)-> bool:
        if box.volume > self.remaining_volume:
            print("Element too large to fit into container")
            return False
        if not self.check_coordinates_in_container(box):
            print("Element is outside the container")
            return False
        if not self.check_fit_with_others_boxes(box):
            print("Element collides with others")
            return False
        return True
               

    def add_box_at_coordinates(self, box: Box,
                               coordinates: object) -> int:  # Python doesn't support function overloading dogshit language
        box.coordinates = coordinates
        self.packed.append(box)
        self.remaining_volume = self.calculate_remaining_volume()
        return self.remaining_volume
    

    def check_fit_in_selected_position(self, box: Box, position) -> bool:
        raise NotImplementedError

    def check_fit_in_default_position(self, box: Box) -> bool:
        # Should check if box is able to fit in (0,0,0) coordinatess
        raise NotImplementedError

    def check_box_collision(self: Box, checked_box: Box) -> bool:
        if self.coordinates["x"] < checked_box.coordinates["x"] < checked_box.coordinates["x"] + checked_box.width:
            return False

        return True

    def assign_box_position(self):

        return


