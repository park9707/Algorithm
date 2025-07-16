import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
move = ((0, 1), (1, 0), (0, -1), (-1, 0))
group = {0: 0}
group_num = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not visited[i][j]:
            q = deque([[i, j]])
            group_num += 1
            visited[i][j] = group_num
            cnt = 1
            while q:
                x, y = q.popleft()
                for dx, dy in move:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == 0 and not visited[nx][ny]:
                            q.append([nx, ny])
                            visited[nx][ny] = group_num
                            cnt += 1

            group[group_num] = cnt

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            g = set()
            for di, dj in move:
                ni = i + di
                nj = j + dj

                if 0 <= ni < n and 0 <= nj < m:
                    if board[ni][nj] == 0:
                        g.add(visited[ni][nj])

            for num in g:
                board[i][j] += group[num]

            board[i][j] = board[i][j] % 10

for i in range(n):
    print(''.join(map(str, board[i])))
