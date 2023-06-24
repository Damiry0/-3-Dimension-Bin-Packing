def check_rect_collision(rect_1, rect_2, dim_1, dim_2):
    rect_1_dim = rect_1.get_packing_configuration()
    rect_2_dim = rect_2.get_packing_configuration()

    cx1 = rect_1.position[dim_1] + rect_1_dim[dim_1] / 2
    cy1 = rect_1.position[dim_2] + rect_1_dim[dim_2] / 2
    cx2 = rect_2.position[dim_1] + rect_2_dim[dim_1] / 2
    cy2 = rect_2.position[dim_2] + rect_2_dim[dim_2] / 2

    ix = max(cx1, cx2) - min(cx1, cx2)
    iy = max(cy1, cy2) - min(cy1, cy2)

    return ix < (rect_1_dim[dim_1] + rect_2_dim[dim_1]) / 2 and iy < (rect_1_dim[dim_2] + rect_2_dim[dim_2]) / 2


def box_collision(box1, box2):
    return (check_rect_collision(box1, box2, 0, 1) and
            check_rect_collision(box1, box2, 1, 2) and
            check_rect_collision(box1, box2, 0, 2))





