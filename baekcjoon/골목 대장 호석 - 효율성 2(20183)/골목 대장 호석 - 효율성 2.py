import sys
import heapq
input = sys.stdin.readline


def dijkstra(start, end, maximum):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    q = [[0, start]]
    while q:
        cost, now = heapq.heappop(q)

        if cost > dist[now]:
            continue

        for next_node, next_cost in node[now]:
            d = next_cost + cost
            if d > c:
                continue
            if next_cost <= maximum and d < dist[next_node]:
                heapq.heappush(q, [d, next_node])
                dist[next_node] = d

    return dist[end] != float('inf')


n, m, a, b, c = map(int, input().split())
node = [[] for _ in range(n + 1)]
costs = set()
ans = float('inf')

for _ in range(m):
    n1, n2, cos = map(int, input().split())
    node[n1].append([n2, cos])
    node[n2].append([n1, cos])
    costs.add(cos)

costs = sorted(costs)
left, right = 0, len(costs)

while left < right:
    mid = (left + right) // 2
    if dijkstra(a, b, costs[mid]):
        ans = costs[mid]
        right = mid
    else:
        left = mid + 1

print(ans if ans != float('inf') else -1)