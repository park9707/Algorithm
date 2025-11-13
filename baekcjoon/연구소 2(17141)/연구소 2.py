import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
start = []
space = 0
move = ((0, 1), (1, 0), (0, -1), (-1, 0))
ans = float('inf')

for i in range(n):
    temp = list(map(int, input().split()))
    space += n - temp.count(1)
    for j in range(n):
        if temp[j] == 2:
            start.append([i, j])
    board.append(temp)

for s in combinations(start, m):
    arr = s
    visited = [[False] * n for _ in range(n)]
    cnt = len(s)
    for x, y in s:
        visited[x][y] = True
    for i in range(250):
        new_arr = []
        for x, y in arr:
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                    if not visited[nx][ny]:
                        new_arr.append([nx, ny])
                        visited[nx][ny] = True
                        cnt += 1

        if len(new_arr) == 0:
            break
        arr = new_arr

    if cnt == space:
        ans = min(i, ans)

print(ans if ans != float('inf') else -1)