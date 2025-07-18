import sys
input = sys.stdin.readline

v, e = map(int, input().split())
dist = [[float('inf')] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = float('inf')
for i in range(1, v + 1):
    ans = min(ans, dist[i][i])

print(ans if ans != float('inf') else -1)