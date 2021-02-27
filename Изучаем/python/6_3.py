"""
Алгори́тм волново́й трассиро́вки (волновой алгоритм, алгоритм Ли) —
алгоритм поиска пути, алгоритм поиска кратчайшего пути на планарном графе.
Принадлежит к алгоритмам, основанным на методах поиска в ширину.
"""

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


def found(pathArr, finPoint):
    weight = 1
    for i in range(len(pathArr) * len(pathArr[0])):
        weight += 1
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == (weight - 1):
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight
                    if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight
                    if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight

                    if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                        pathArr[finPoint[0]][finPoint[1]] = weight
                        return True
    return False


def printPath(pathArr, finPoint):
    y = finPoint[0]
    x = finPoint[1]
    weight = pathArr[y][x]
    result = list(range(weight))
    while (weight):
        weight -= 1
        if y > 0 and pathArr[y - 1][x] == weight:
            y -= 1
            result[weight] = 'down'
        elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
            result[weight] = 'up'
            y += 1
        elif x > 0 and pathArr[y][x - 1] == weight:
            result[weight] = 'right'
            x -= 1
        elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
            result[weight] = 'left'
            x += 1

    return result[1:]


def can_pass(matrix, first, second):

    right_digit = matrix[first[0]][first[1]] # 0 .. 10 по условию задачи

    labirynth = []
    for row in matrix:
        labirynth.append(list(row))

    for i in range(len(labirynth)):
        for j in range(len(labirynth[0])) :
            if labirynth[i][j] != right_digit:
                labirynth[i][j] = -1
            else:
                labirynth[i][j] = 0

    labirynth[first[0]][first[1]] = 1

    r =  found(labirynth, second)
    result = printPath(labirynth, second)

    for i in labirynth:
        for line in i:
            print("{:^3}".format(line), end=" ")
        print("")
    print(result)

    return r



print(can_pass(m2, (2,5), (0,4)))

