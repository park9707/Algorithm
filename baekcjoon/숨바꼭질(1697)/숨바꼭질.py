from collections import deque

n, k = map(int, input().split())
MAX = 100000
dist = [0] * (MAX + 1)


def bfs():
    q = deque()
    q.append(n)
    while q:
        i = q.popleft()
        if i == k:
            print(dist[i])
            break
        for j in (i - 1, i + 1, i * 2):
            if 0 <= j <= MAX and not dist[j]:
                dist[j] = dist[i] + 1
                q.append(j)


bfs()