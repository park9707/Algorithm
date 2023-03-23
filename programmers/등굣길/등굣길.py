from collections import deque


def solution(m, n, puddles):
    maps = [[0] * m for _ in range(n)]
    maps[0][1] = maps[1][0] = 1
    for a, b in puddles:
        maps[b-1][a-1] = -1
    dx = [0, 1]
    dy = [1, 0]
    q = deque([(1, 0), (0, 1)])
    while q:
        x, y = q.popleft()
        if x == m - 1 and y == n - 1 or maps[y][x] == -1:
            continue
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < m and ny < n and maps[ny][nx] != -1:
                if maps[ny][nx] == 0:
                    q.append((nx, ny))
                maps[ny][nx] += maps[y][x]

    return maps[n - 1][m - 1] % 1000000007