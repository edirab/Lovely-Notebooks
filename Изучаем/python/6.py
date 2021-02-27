"""
 If you have solved the "How to find friends" mission, then you already know how to check for the existence of a path in graphs. Let's try to add something more to that problem.

You are given a matrix (2D array) and the coordinates (row and column) of two cells with the same value. The matrix consists of digits. You may move to neighbouring cells either horizontally or vertically provided the values of the origin and destination cells are equal. You should determine if a path exists between two given cells.

A matrix is represented as a tuple of tuples with digits. Coordinates are represented as a tuple with two numbers: row and column. The result should be any value which can be converted into a boolean. If a path exists, then return True. Return False if there is none.

 Input: Three arguments. A matrix as a tuple of tuples with integers, first and second cell coordinates as tuples of two integers.

Output: The existence of a path between two given cells as a boolean or a value that can be converted to boolean.
Example:
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 2), (0, 5)) == True, 'First example'
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 3), (6, 0)) == False,


How it is used: Sometimes we don't need the full pathfinding algorithms implementation and can use simplified realisation of these algorithms. It can be an useful skill to find a simple ways.

Precondition:
1 < len(matrix) ≤ 10
all(1 < len(row) ≤ 10 for row in matrix)
all(all(0 ≤ x < 10 for x in row) for row in matrix)
matrix[first[0]][first[1]] == matrix[second[0]][second[1]]
first != second
"""
from pprint import pprint

m1 = ((0, 0, 0, 0, 0, 0),
(0, 2, 2, 2, 3, 2),
(0, 2, 0, 0, 0, 2),
(0, 2, 0, 2, 0, 2),
(0, 2, 2, 2, 0, 2),
(0, 0, 0, 0, 0, 2),
(2, 2, 2, 2, 2, 2))

m2 = (
    (4, 6, 4, 9, 9, 9, 6, 6, 4),
    (4, 6, 9, 9, 9, 9, 4, 6, 6),
    (9, 9, 6, 9, 4, 9, 9, 4, 6),
    (9, 4, 4, 4, 6, 9, 9, 4, 6)
)

# point = (строкаб столбец)

def can_go_up(m, point):
    rows = len(m)
    cols = len(m[0])
    return (point[0] > 0) and (m[point[0]][point[1]] == m[point[0]-1][point[1]])


def can_go_down(m, point):
    rows = len(m)
    cols = len(m[0])
    #print(rows, cols)
    return (point[0] < rows - 1) and (m[point[0]][point[1]] == m[point[0]+1][point[1]])


def can_go_right(m, point):
    rows = len(m)
    cols = len(m[0])
    # print(m[point[0]][point[1]] , m[point[0]][point[1]+1])
    return (point[1] < cols - 1) and (m[point[0]][point[1]] == m[point[0]][point[1]+1])


def can_go_left(m, point):
    rows = len(m)
    cols = len(m[0])
    return (point[1] > 0) and (m[point[0]][point[1]] == m[point[0]][point[1]-1])


def find_path(m, first, second):

    # Создадим копию матрицы, чтобы помечать посещённые клетки.
    # Потребуется преобразовать в список
    m_copy = []
    for elem in m:
        m_copy.append(list(elem))

    m_copy[first[0]][first[1]] = 'X'
    pprint(m_copy)

    if first == second:
        return True
    #point = [first[0], first[1]]

    if can_go_right(m, first):
        # print("moving right")
        return find_path(m_copy, (first[0], first[1]+1), second)

    if can_go_up(m, first):
        # print("moving up")
        return find_path(m_copy, (first[0]-1, first[1]), second)

    if can_go_left(m, first):
        # print("moving left")
        return find_path(m_copy, (first[0], first[1]-1), second)

    if can_go_down(m, first):
        # print("moving down")
        return find_path(m_copy, (first[0]+1, first[1]), second)

    return False


def can_pass(m, first, second):
    return find_path(m, first, second)

# test
def test_dir():
    print("Test 1: ", can_go_up(m1, (2, 2)))
    print("Test 2: ", can_go_down(m1, (3, 2)))
    print("Test 3: ", can_go_right(m1, (0, 4)))
    print("Test 4: ", can_go_left(m1, (0, 0)))

test_dir()

#print(can_pass(m1, (3, 2), (0, 5)))
#print(can_pass(m1, (3, 3), (6, 0)))

print(can_pass(m2, (2,5), (0,4)))