import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
bead = [[0, 0], [0, 0]]
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = deque([[0, 0, 0, 0, 0]])

for i in range(n):
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == 'R':
            q[0][0] = i
            q[0][1] = j
            s[j] = '.'
        elif s[j] == 'B':
            q[0][2] = i
            q[0][3] = j
            s[j] = '.'
    maps.append(s)


def tilt(x, y, dx, dy, c):
    while True:
        nx = x + dx
        ny = y + dy

        if maps[nx][ny] == '#':
            break

        if maps[nx][ny] == 'O':
            return -1, -1, 0

        x = nx
        y = ny
        c += 1
    return x, y, c


def bfs():
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        temp_rx, temp_ry, temp_bx, temp_by = rx, ry, bx, by
        if cnt == 10:
            break
        for dx, dy in move:
            bx, by, bc = tilt(temp_bx, temp_by, dx, dy, 0)
            if bx == -1:
                continue

            rx, ry, rc = tilt(temp_rx, temp_ry, dx, dy, 0)
            if rx == -1:
                return cnt + 1

            if bx == rx and by == ry:
                if bc < rc:
                    rx -= dx
                    ry -= dy
                elif bc > rc:
                    bx -= dx
                    by -= dy

            if not visited[rx][ry][bx][by]:
                visited[rx][ry][bx][by] = True
                q.append([rx, ry, bx, by, cnt + 1])

    return -1


print(bfs())
