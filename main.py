def check_rect_collision(rect_1, rect_2, x, y):
    d1 = rect_1.get_packing_configuration()
    d2 = rect_2.get_packing_configuration()

    cx1 = rect_1.position[x] + d1[x] / 2
    cy1 = rect_1.position[y] + d1[y] / 2
    cx2 = rect_2.position[x] + d2[x] / 2
    cy2 = rect_2.position[y] + d2[y] / 2

    ix = max(cx1, cx2) - min(cx1, cx2)
    iy = max(cy1, cy2) - min(cy1, cy2)

    return ix < (d1[x] + d2[x]) / 2 and iy < (d1[y] + d2[y]) / 2


def box_collision(box1, box2):
    return (check_rect_collision(box1, box2, 0, 1) and
            check_rect_collision(box1, box2, 1, 2) and
            check_rect_collision(box1, box2, 0, 2))





