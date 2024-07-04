import sys, heapq
input = sys.stdin.readline


def dijkstra(start):
    q = [(0, start)]
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if d > dist[now]:
            continue
        for next_n, t in graph[now]:
            cost = d + t
            if dist[next_n] > cost:
                dist[next_n] = cost
                heapq.heappush(q, (cost, next_n))


N, M = map(int, input().split())
enemy_vision = list(map(int, input().split()))
enemy_vision[-1] = 0
graph = [[] for _ in range(N)]
dist = [float('inf')] * N

for _ in range(M):
    a, b, t = map(int, input().split())
    if enemy_vision[a] or enemy_vision[b]:
        continue
    graph[a].append((b, t))
    graph[b].append((a, t))

dijkstra(0)
print(dist[-1] if dist[-1] != float('inf') else -1)