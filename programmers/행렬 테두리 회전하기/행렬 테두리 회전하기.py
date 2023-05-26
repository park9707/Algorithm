def solution(rows, columns, queries):
    answer = []
    maps = [[(j * columns) + i for i in range(1, columns + 1)] for j in range(rows)]
    for x1, y1, x2, y2 in list(map(lambda a: (a[0] - 1, a[1] - 1, a[2] - 1, a[3] - 1), queries)):
        stack1 = [maps[x1][y1]]
        stack2 = [maps[x2][y2]]
        result = min(stack1[0], stack2[0])
        x = x2 - x1
        y = y2 - y1
        while y > 0:
            y -= 1
            tmp1 = stack1.pop()
            tmp2 = stack2.pop()
            stack1.append(maps[x1][y2 - y])
            stack2.append(maps[x2][y1 + y])
            maps[x1][y2 - y] = tmp1
            maps[x2][y1 + y] = tmp2
            result = min(result, tmp1, tmp2)

        while x > 0:
            x -= 1
            tmp1 = stack1.pop()
            tmp2 = stack2.pop()
            stack1.append(maps[x2 - x][y2])
            stack2.append(maps[x1 + x][y1])
            maps[x2 - x][y2] = tmp1
            maps[x1 + x][y1] = tmp2
            result = min(result, tmp1, tmp2)
        answer.append(result)
    return answer
