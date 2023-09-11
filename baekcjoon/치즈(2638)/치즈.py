import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0] * m for _ in range(n)]
maps = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    cnt += tmp.count(1)
    maps.append(tmp)


def check(x, y, t):
    for dx, dy in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] != t:
                if maps[nx][ny] == 1:
                    c[nx, ny] += 1
                    if c[nx, ny] == 2:
                        arr.add((nx, ny))
                else:
                    visited[nx][ny] = t
                    check(nx, ny, t)


cnt = t = 0
while cnt:
    arr = set()
    c = defaultdict(int)
    t += 1
    visited[0][0] = t
    check(0, 0, t)
    cnt -= len(arr)
    for x, y in arr:
        maps[x][y] = 0

    cnt += 1

print(cnt)