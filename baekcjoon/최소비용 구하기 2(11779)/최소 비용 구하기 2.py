import sys
import heapq
input = sys.stdin.readline


def dijkstra():
    parents = [i for i in range(n + 1)]
    q = [(0, start)]
    while q:
        c, now = heapq.heappop(q)

        if now == end:
            break

        if node[now] < c:
            continue

        for next_node, cost in maps[now]:
            next_cost = c + cost
            if next_cost < node[next_node]:
                node[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))
                parents[next_node] = now

    i = end
    path = [end]
    while i != start:
        path.append(parents[i])
        i = parents[i]

    print(c)
    print(len(path))
    print(*path[::-1])


n = int(input())
m = int(input())
maps = [[] for _ in range(n + 1)]
node = [float('inf')] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append([b, c])

start, end = map(int, input().split())
dijkstra()