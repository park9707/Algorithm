import sys
from collections import deque
input = sys.stdin.readline

n, m, fuel = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
taxi = list(map(lambda x: int(x) - 1, input().split()))
goal = {}
for _ in range(m):
    start_x, start_y, goal_x, goal_y = map(lambda x: int(x) - 1, input().split())
    maps[start_x][start_y] = 2
    goal[start_x, start_y] = [goal_x, goal_y]
move = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def find_customer(x, y, fuel):
    if maps[x][y] == 2:
        return [x, y, fuel]
    q = deque([[x, y, fuel]])
    visited[x][y] = 1
    candi = []
    p = 0
    while q:
        x, y, f = q.popleft()
        if p > f:
            continue
        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny:
                continue

            if maps[nx][ny] == 1 or visited[nx][ny] == 1:
                continue

            if maps[nx][ny] == 2:
                candi.append([nx, ny])
                visited[nx][ny] = 1
                p = f
                continue

            if f > 1:
                visited[nx][ny] = 1
                q.append([nx, ny, f - 1])

    if candi:
        candi.sort(key=lambda x: (x[0], x[1]))
        return [candi[0][0], candi[0][1], p-1]
    return [-1, -1, -1]


def go(x, y, gx, gy, fuel):
    if fuel <= 0:
        return 0
    q = deque([[x, y, fuel]])
    visited[x][y] = 2
    while q:
        x, y, f = q.popleft()

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny:
                continue

            if maps[nx][ny] == 1 or visited[nx][ny] == 2:
                continue

            if nx == gx and ny == gy:
                return fuel-f+1

            if f > 1:
                visited[nx][ny] = 2
                q.append([nx, ny, f-1])

    return 0


for i in range(m):
    visited = [[0] * n for _ in range(n)]
    x, y, fuel = find_customer(taxi[0], taxi[1], fuel)
    if x == -1:
        break
    maps[x][y] = 0
    goal_x, goal_y = goal[x, y]
    refuel = go(x, y, goal_x, goal_y, fuel)
    if refuel == 0:
        fuel = -1
        break
    fuel += refuel
    taxi = [goal_x, goal_y]

print(fuel)
