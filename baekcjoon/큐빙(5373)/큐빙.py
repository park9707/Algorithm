import sys
input = sys.stdin.readline


def rotate_2d(d, side):
    next_cube_2d = [[''] * 3 for _ in range(3)]
    for x in range(3):
        for y in range(3):
            next_x, next_y = rotate_2d_num[x][y][d]
            next_cube_2d[next_x][next_y] = cube[side][x][y]
    cube[side] = next_cube_2d


def rotate_3d(d, side):
    rotate_side = rotate_side_num[side]
    if side < 2:
        y = 0 if side == 0 else 2
        temp = cube[rotate_side[0]][y]
        if d == 0:
            cube[rotate_side[0]][y] = cube[rotate_side[1]][y]
            for i in range(1, 3):
                cube[rotate_side[i]][y] = cube[rotate_side[i+1]][y]
            cube[rotate_side[3]][y] = temp
        else:
            cube[rotate_side[0]][y] = cube[rotate_side[-1]][y]
            for i in range(-1, -3, -1):
                cube[rotate_side[i]][y] = cube[rotate_side[i-1]][y]
            cube[rotate_side[1]][y] = temp

    elif 2 <= side < 4:
        y = [0, 2] if side == 2 else [2, 0]
        temp = [cube[rotate_side[0]][i][y[1]] for i in range(3)][::-1]
        if d == 0:
            for j in range(1, 4):
                cube[rotate_side[0]][-j][y[1]] = cube[rotate_side[1]][j-1][y[0]]
            for i in range(1, 3):
                for j in range(3):
                    cube[rotate_side[i]][j][y[0]] = cube[rotate_side[i+1]][j][y[0]]
            for j in range(3):
                cube[rotate_side[3]][j][y[0]] = temp[j]
        else:
            for j in range(1, 4):
                cube[rotate_side[0]][-j][y[1]] = cube[rotate_side[-1]][j-1][y[0]]
            for i in range(-1, -3, -1):
                for j in range(3):
                    cube[rotate_side[i]][j][y[0]] = cube[rotate_side[i-1]][j][y[0]]
            for j in range(3):
                cube[rotate_side[1]][j][y[0]] = temp[j]

    else:
        temp = []
        xy = [0, 2] if side == 4 else [2, 0]
        k = 0
        for i in range(3):
            temp.append(cube[rotate_side[0]][xy[1]][i])
        for i in range(3):
            temp.append(cube[rotate_side[1]][i][xy[0]])
        for i in range(2, -1, -1):
            temp.append(cube[rotate_side[2]][xy[0]][i])
        for i in range(2, -1, -1):
            temp.append(cube[rotate_side[3]][i][xy[1]])

        if (d == 0 and side == 4) or (d == 1 and side == 5):
            for i in range(2, -1, -1):
                cube[rotate_side[3]][i][xy[1]] = temp[k]
                k += 1
            for i in range(3):
                cube[rotate_side[0]][xy[1]][i] = temp[k]
                k += 1
            for i in range(3):
                cube[rotate_side[1]][i][xy[0]] = temp[k]
                k += 1
            for i in range(2, -1, -1):
                cube[rotate_side[2]][xy[0]][i] = temp[k]
                k += 1
        else:
            for i in range(3):
                cube[rotate_side[1]][i][xy[0]] = temp[k]
                k += 1
            for i in range(2, -1, -1):
                cube[rotate_side[2]][xy[0]][i] = temp[k]
                k += 1
            for i in range(2, -1, -1):
                cube[rotate_side[3]][i][xy[1]] = temp[k]
                k += 1
            for i in range(3):
                cube[rotate_side[0]][xy[1]][i] = temp[k]
                k += 1


side_num = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'F': 4, 'B': 5}
direction = {'-': 0, '+': 1}
rotate_side_num = {0: (5, 3, 4, 2), 1: (5, 2, 4, 3), 2: (5, 0, 4, 1),
                   3: (5, 1, 4, 0), 4: (0, 3, 1, 2), 5: (0, 3, 1, 2)}
rotate_2d_num = ((((2, 0), (0, 2)), ((1, 0), (1, 2)), ((0, 0), (2, 2))),
                 (((2, 1), (0, 1)), ((1, 1), (1, 1)), ((0, 1), (2, 1))),
                 (((2, 2), (0, 0)), ((1, 2), (1, 0)), ((0, 2), (2, 0))))
n = int(input())
for _ in range(n):
    # 상 하 좌 우 앞 뒤
    cube = [[['w'] * 3 for _ in range(3)],
            [['y'] * 3 for _ in range(3)],
            [['g'] * 3 for _ in range(3)],
            [['b'] * 3 for _ in range(3)],
            [['r'] * 3 for _ in range(3)],
            [['o'] * 3 for _ in range(3)]]
    input()  # 필요 없는 정보
    location = list(input().split())
    for lc in location:
        rotate_2d(direction[lc[1]], side_num[lc[0]])
        rotate_3d(direction[lc[1]], side_num[lc[0]])
    for i in range(3):
        print(''.join(cube[0][i]))