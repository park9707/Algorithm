import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
mode = [[],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]]]
maps = []
cctv = []
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j] != 0:
            if maps[i][j] != 6:
                cctv.append([maps[i][j], i, j])


def dfs(cctv, maps):
    if cctv:
        num, x, y = cctv[0]
        for i in mode[num]:
            temp = copy.deepcopy(maps)
            fill(x, y, temp, i)
            dfs(cctv[1:], temp)
    else:
        global answer
        cnt = 0
        for i in range(n):
            cnt += maps[i].count(0)
        answer = min(cnt, answer)


def fill(x, y, maps, mode):
    for k in mode:
        dx, dy = move[k]
        nx = x
        ny = y
        while True:
            nx += dx
            ny += dy
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                break

            if maps[nx][ny] == 6:
                break

            elif maps[nx][ny] == 0:
                maps[nx][ny] = -1


answer = float("inf")
dfs(cctv, maps)
print(answer)