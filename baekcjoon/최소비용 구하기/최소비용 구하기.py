import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for c, v in graph[now]:
            if dist + c < distance[v]:
                distance[v] = dist + c
                heapq.heappush(heap, (dist + c, v))

dijkstra(start)

print(distance[end])

