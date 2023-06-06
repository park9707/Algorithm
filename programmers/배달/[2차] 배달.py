import heapq


def solution(N, road, K):
    maps = [[] for _ in range(N + 1)]
    dist = [float('inf')] * (N + 1)
    dist[1] = 0

    for a, b, c in road:
        maps[a].append([b, c])
        maps[b].append([a, c])

    q = []
    heapq.heappush(q, [0, 1])

    while q:
        t, n = heapq.heappop(q)
        for i, d in maps[n]:
            if t + d < dist[i]:
                dist[i] = t + d
                heapq.heappush(q, [t + d, i])

    return len([i for i in dist[1:] if i <= K])
