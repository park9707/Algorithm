import sys, heapq, collections
input = sys.stdin.readline

n, m = map(int, input().split())
sub = collections.defaultdict(list)
degree = [0] * (n + 1)
q = []

for _ in range(m):
    a, b = map(int, input().split())
    sub[a].append(b)
    degree[b] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(q, i)

while q:
    p = heapq.heappop(q)
    print(p, end=' ')
    for s in sub.get(p, []):
        degree[s] -= 1
        if degree[s] == 0:
            heapq.heappush(q, s)