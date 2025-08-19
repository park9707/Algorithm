import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    dist = [float('inf')] * n
    dist[start] = 0
    q = [[0, start]]
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue

        for next_node, cost in road[now]:
            next_dist = d + cost
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(q, [next_dist, next_node])

    result = 0
    for i in range(n):
        if dist[i] <= m:
            result += items[i]

    return result


n, m, r = map(int, input().split())
items = list(map(int, input().split()))
road = [[] for _ in range(n)]
ans = 0
for _ in range(r):
    a, b, c = map(int, input().split())
    road[a-1].append([b-1, c])
    road[b-1].append([a-1, c])

for i in range(n):
    ans = max(ans, dijkstra(i))

print(ans)