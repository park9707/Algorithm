from collections import deque

def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque([(0, 0)])
    maps[0][0] = 0
    n = len(maps)-1
    m = len(maps[0])-1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n or ny < 0 or ny > m:
                continue

            if maps[nx][ny] == 0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1
                queue.append((nx, ny))

    if maps[n][m] == 1:
        if n+m == 1:
            return 2
        else:
            return -1
    return maps[n][m] + 1