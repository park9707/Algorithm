import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
        return parents[x]
    return x


def union(a, b):
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n, Q = map(int, input().split())
parents = [i for i in range(n + 1)]
edges = []
total_t = total_c = 0
for _ in range(Q):
    a, b, c, t = map(int, input().split())
    edges.append([c, t, a, b])

edges.sort()

for i in range(Q):
    c, t, a, b = edges[i]
    parents_a = find(a)
    parents_b = find(b)
    if parents_a != parents_b:
        union(parents_a, parents_b)
        total_c += c
        total_t = max(t, total_t)

for i in range(2, n + 1):
    if parents[i] == i:
        print(-1)
        exit(0)

print(total_t, total_c)