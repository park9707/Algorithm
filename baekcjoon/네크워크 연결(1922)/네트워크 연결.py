import sys
import heapq
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n = int(input())
m = int(input())
q = []
ans = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(q, [c, a, b])

parents = [i for i in range(n + 1)]
while q:
    c, a, b = heapq.heappop(q)
    if find(a) != find(b):
        union(a, b)
        ans += c

print(ans)