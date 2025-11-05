import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
q = deque()
land = deque([[-1, -1, -1]])
land_num = 2
move = ((0, 1), (1, 0), (0, -1), (-1, 0))

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            q.append([i, j])
            maps[i][j] = land_num
            while q:
                x, y = q.popleft()
                for dx, dy in move:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if maps[nx][ny] == 1:
                            q.append([nx, ny])
                            maps[nx][ny] = land_num
                        elif maps[nx][ny] == 0 and (land[-1][0] != x or land[-1][1] != y):
                            land.append([x, y, land_num])

            land_num += 1

ans = float('inf')
land.popleft()
visited = [[[0, 0] for _ in range(n)] for _ in range(n)]
while land:
    x, y, land_num = land.popleft()
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 0:
            if visited[nx][ny][0] == 0:
                if visited[nx][ny][1] < ans // 2 + 1:
                    continue
                visited[nx][ny][0] = land_num
                visited[nx][ny][1] = visited[x][y][1] + 1
                land.append([nx, ny, land_num])
            elif visited[nx][ny][0] != land_num:
                ans = min(ans, visited[x][y][1] + visited[nx][ny][1])
                
print(ans)