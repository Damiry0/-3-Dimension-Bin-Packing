# This is a Layer Building Algorithm based on the Loh and Nee (1992)
# Layer Building heuristics. Each box is rotated and placed into groups by height.
# At first the groups will be of boxes of the same height, but further on, a tolerance
# parameter will be implemented so that given box height y, boxes of height b*y can also be
# placed in the same group. These groups can then be sorted by decreasing base area, or how it will be
# at first implemented: they will be sorted by depth or width parameter, to get a contiguous,
# homogenous layer. Each layers will be placed at the back of the box, with subsequent layers being
# placed in front of them, this way, we can achieve some sort of packing standardization. Later on,
# this algorithm will be modified in order to achieve the best possible fit options.
#
#
# Algorithm steps:
# 1. Get Boxes data
# 2. Rotate Boxes and group Boxes into layers
# First group will be formed by biggest edge, this will be tested on boxes which sizes vary from 1 to 10 in each
# dimension, the biggest dimension will be chosen
# 3. Place layers in box
# 4. Check for remaining space





