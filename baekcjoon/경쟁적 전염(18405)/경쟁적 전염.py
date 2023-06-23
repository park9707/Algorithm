import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, ix, iy = map(int, input().split())
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False] * n for _ in range(n)]
t = s
arr = []
q = deque([[ix-1, iy-1, 0]])
visited[ix-1][iy-1] = True
while q:
    x, y, cnt = q.popleft()
    if s <= cnt:
        continue
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] != 0:
                s = cnt + 1
                arr.append(board[nx][ny])
            elif not visited[nx][ny]:
                if s - cnt - 1 > 0:
                    visited[nx][ny] = True
                    q.append([nx, ny, cnt + 1])

arr.sort()
print(arr[0] if arr else board[ix-1][iy-1])
