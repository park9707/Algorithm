import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
if n == 1 and m == 1:
    print(1)
    exit()
board = [[int(i) for i in list(input().rstrip())] for _ in range(n)]
q = deque([[0, 0, 1, k]])
visited = [[-1] * m for _ in range(n)]
visited[0][0] = 10
move = [[0, 1], [1, 0], [-1, 0], [0, -1]]

while q:
    x, y, num, d = q.popleft()
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if nx == n - 1 and ny == m - 1:
                print(num + 1)
                exit()
            if board[nx][ny] == 0:
                if visited[nx][ny] < d:
                    visited[nx][ny] = d
                    q.append([nx, ny, num + 1, d])
            elif board[nx][ny] == 1:
                if d > 0 and visited[nx][ny] < d - 1:
                    visited[nx][ny] = d - 1
                    q.append([nx, ny, num + 1, d - 1])

else:
    print(-1)