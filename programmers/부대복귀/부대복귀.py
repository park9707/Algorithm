from collections import deque


def solution(n, roads, sources, destination):
    maps = [[] * (n + 1) for _ in range(n + 1)]
    d = [-1] * (n + 1)
    for a, b in roads:
        maps[a].append(b)
        maps[b].append(a)

    def bfs(des):
        q = deque([des])
        d[des] = 0
        while q:
            a = q.popleft()
            for i in maps[a]:
                if d[i] == -1:
                    q.append(i)
                    d[i] = d[a] + 1
    bfs(destination)
    return [d[s] for s in sources]
