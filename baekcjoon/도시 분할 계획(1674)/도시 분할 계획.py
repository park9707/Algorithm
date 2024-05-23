import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    if a < b:
        parents[a] = b
    else:
        parents[b] = a


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
road = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[2])
ans = 0
max_c = 0

for s, e, c in road:
    s, e = find(s), find(e)
    if s != e:
        union(s, e)
        ans += c
        max_c = max(max_c, c)

print(ans - max_c)