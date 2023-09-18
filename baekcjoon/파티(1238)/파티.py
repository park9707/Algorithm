import sys, heapq
input = sys.stdin.readline


def dijkstra(road):
    node = [float('inf')] * (n + 1)
    node[x] = 0
    q = [(0, x)]

    while q:
        cost, now = heapq.heappop(q)
        if node[now] < cost:
            continue

        for next_node, next_cost in road[now]:
            temp_cost = cost + next_cost
            if temp_cost < node[next_node]:
                node[next_node] = temp_cost
                heapq.heappush(q, (temp_cost, next_node))

    return node


n, m, x = map(int, input().rstrip().split())
start_road = [[] for _ in range(m + 1)]
end_road = [[] for _ in range(m + 1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    start_road[b].append([a, c])
    end_road[a].append([b, c])

start_node = dijkstra(start_road)
end_node = dijkstra(end_road)
answer = 0

for i in range(1, n + 1):
    answer = max(answer, start_node[i] + end_node[i])
print(answer)
