import sys
sys.setrecursionlimit(100000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(maps):
    maps = [list(map(str, i)) for i in maps]
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                answer.append(dfs(j, i, maps))

    return sorted(answer) if answer else [-1]


def dfs(x, y, maps):
    cnt = int(maps[y][x])
    maps[y][x] = 'X'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] != 'X':
            cnt += dfs(nx, ny, maps)

    return cnt


print(solution(["XXX", "XXX", "XXX"]))