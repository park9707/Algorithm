import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())
road = []
for _ in range(M):
    road.append(list(map(int, input().split())))

parents = [i for i in range(N + 1)]
road.sort(key=lambda x: x[2])
ans = 0
connected_road = 0

for s, e, c in road:
    if find(s) != find(e):
        union(parents[s], parents[e])
        connected_road += 1
    else:
        ans += c

if connected_road == N - 1:
    print(ans)
else:
    print(-1)
