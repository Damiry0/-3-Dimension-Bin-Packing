def check_box_wall_collision(box1, box2, axis1, axis2):
    box1_dim = box1.get_packing_configuration()
    box2_dim = box2.get_packing_configuration()

    check_axis1_box1 = box1.position[axis1] + box1_dim[axis1] / 2
    check_axis2_box1 = box1.position[axis2] + box1_dim[axis2] / 2
    check_axis1_box2 = box2.position[axis1] + box2_dim[axis1] / 2
    check_axis2_box2 = box2.position[axis2] + box2_dim[axis2] / 2

    intersect_x_axis = max(check_axis1_box1, check_axis1_box2) - min(check_axis1_box1, check_axis1_box2)
    intersect_y_axis = max(check_axis2_box1, check_axis2_box2) - min(check_axis2_box1, check_axis2_box2)

    return intersect_x_axis < (box1_dim[axis1] + box2_dim[axis1]) / 2 and intersect_y_axis < (box1_dim[axis2] + box2_dim[axis2]) / 2


def box_collision(box1, box2):
    return (check_box_wall_collision(box1, box2, 0, 1) and
            check_box_wall_collision(box1, box2, 1, 2) and
            check_box_wall_collision(box1, box2, 0, 2))





