import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for c, v in graph[now]:
            if dist+c < distance[v]:
                distance[v] = dist+c
                heapq.heappush(heap, (dist+c, v))

dijkstra(1)
print(distance[n])