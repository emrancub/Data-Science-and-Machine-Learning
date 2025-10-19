# CoordinateTuples.py
# A list of coordinate tuples and a function to calculate distances.

import math

points = ((0,0), (3,4), (6,8))

def distance(p1, p2):
    return math.dist(p1, p2)

if __name__ == '__main__':
    print("Points:", points)
    print("Distance between first and last:", distance(points[0], points[-1]))