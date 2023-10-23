import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    dist[i+1][i+1] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
