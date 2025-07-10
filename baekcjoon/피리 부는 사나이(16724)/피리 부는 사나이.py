import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
safe_zone = 0


def dfs(x, y):
    global safe_zone

    visited[y][x] = True
    cycle.append([x, y])

    if maps[y][x] == 'U' and y > 0:
        y -= 1
    elif maps[y][x] == 'D' and y < N - 1:
        y += 1
    elif maps[y][x] == 'L' and x > 0:
        x -= 1
    elif maps[y][x] == 'R' and x < M - 1:
        x += 1

    if visited[y][x]:
        if [x, y] in cycle:
            safe_zone += 1
    else:
        dfs(x, y)


for x in range(M):
    for y in range(N):
        if not visited[y][x]:
            cycle = []
            dfs(x, y)

print(safe_zone)