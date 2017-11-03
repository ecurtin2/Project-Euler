import sys
sys.path.append('../customlib')

import numpy as np


def same_side(point1, point2, linept1, linept2):
    """Return true if point1 and point2 are on same side of line defined by linept1, linept2, else false"""
    line = linept2 - linept1
    cp1 = np.cross(line, point1 - linept1)
    cp2 = np.cross(line, point2 - linept1)
    return np.dot(cp1, cp2) >= 0


def point_in_triangle(p, triangle):
    a, b, c, = triangle[0], triangle[1], triangle[2]
    return same_side(p, a, b, c) and same_side(p, b, a, c) and same_side(p, c, a, b)


triangles = np.loadtxt('102.dat', delimiter=',', dtype=int)
triangles = triangles.reshape(len(triangles), 3, 2)

origin = np.array((0, 0))
print(sum(point_in_triangle(origin, t) for t in triangles))
