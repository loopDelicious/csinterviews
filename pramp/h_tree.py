"""
Construct an H-tree, given its center (x and y coordinates), starting_length and depth.

You can assume that you have a drawLine method.

An H-tree can be constructed by starting with a line segment of arbitrary length,
drawing two segments of the same length at right angles to the first through its endpoints,
and continuing in the same vein, reducing (dividing) the length of the line segments drawn at each stage
by sqrt of 2.

    |               |
    |               |
    |- - (x, y) - - |
    |               |
    |          |    |    |
               |- - - - -|
               |         |

"""
import math

def h_tree(x, y, length, depth):
    """ construct an H-tree """

    if depth == 0:
        return None

    x0 = x - length / 2
    x1 = x + length / 2
    y0 = y - length / 2
    y1 = y + length / 2


    drawLine(x0, y0, x0, y1) # left
    drawLine(x1, y0, x1, y1) # right
    drawLine(x0,  y, x1,  y) # middle

    new_length = length / math.sqrt(2)

    h_tree(x0, y0, new_length, depth-1) # lower left
    h_tree(x0, y1, new_length, depth-1) # upper left
    h_tree(x1, y0, new_length, depth-1) # lower right
    h_tree(x1, y1, new_length, depth-1) # upper right

#     Runtime is O(4^D) . . . 4 recursive calls to D depth
#     Space is O(D) . . . recursive calls are sequential
