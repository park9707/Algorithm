import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j, d):
    global cnt
    queue = deque([[i, j]])
    visited[i][j] = 1
    cnt += 1

    while queue:
        x, y = queue.popleft()
        flag = 0

        for _ in range(4):
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not board[nx][ny]:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    cnt += 1
                    flag = 1
                    break

        if flag == 0:
            if board[x - dx[d]][y - dy[d]] != 1:
                queue.append([x - dx[d], y - dy[d]])

            else:
                return cnt


print(bfs(r, c, d))
