"""
Similar Triangles

 This is a mission to check the similarity of two triangles.

You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)

Example:
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False
similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True


"""
from typing import List, Tuple
Coords = List[Tuple[int, int]]


def setBit(int_type, offset):
    mask = 1 << offset
    return (int_type | mask)


def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return (int_type & mask)


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    s1 = (coords_1[0][0] - coords_1[1][0]) ** 2 + (coords_1[0][1] - coords_1[1][1]) ** 2
    s2 = (coords_1[1][0] - coords_1[2][0]) ** 2 + (coords_1[1][1] - coords_1[2][1]) ** 2
    s3 = (coords_1[2][0] - coords_1[0][0]) ** 2 + (coords_1[2][1] - coords_1[0][1]) ** 2

    s4 = (coords_2[0][0] - coords_2[1][0]) ** 2 + (coords_2[0][1] - coords_2[1][1]) ** 2
    s5 = (coords_2[1][0] - coords_2[2][0]) ** 2 + (coords_2[1][1] - coords_2[2][1]) ** 2
    s6 = (coords_2[2][0] - coords_2[0][0]) ** 2 + (coords_2[2][1] - coords_2[0][1]) ** 2

    sides1 = [s1, s2, s3]
    sides2 = [s4, s5, s6]

    sides1.sort()
    sides2.sort()

    scale_factor = sides1[0] / sides2[0]
    #print(s1, s2, s3, s4, s5, s6)

    if sides1[1] / sides2[1] == scale_factor and sides1[2]/sides2[2] == scale_factor:
        return True
    else:
        return False


similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)])
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)])
similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)])
similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)])

assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
print("Coding complete? Click 'Check' to earn cool rewards!")