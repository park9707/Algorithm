import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    rank = list(map(int, input().split()))
    degree = [0] * (n + 1)
    link = [[] for _ in range(n + 1)]
    for i, v in enumerate(rank):
        link[rank[i]].extend(rank[i+1:])
        degree[rank[i]] = i

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in link[b]:
            link[b].remove(a)
            link[a].append(b)
            degree[b] += 1
            degree[a] -= 1
        else:
            link[a].remove(b)
            link[b].append(a)
            degree[a] += 1
            degree[b] -= 1

    q = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)

    if not q:
        print('IMPOSSIBLE')
        continue

    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for i in link[v]:
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)

    if sum(degree) > 0:
        print('IMPOSSIBLE')
    else:
        print(*ans)