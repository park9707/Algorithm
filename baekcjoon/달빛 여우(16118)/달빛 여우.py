import sys, heapq
input = sys.stdin.readline


def fox_dijkstra():
    q = [[0, 1]]
    while q:
        d, now = heapq.heappop(q)
        if fox_dist[now] < d:
            continue

        for next_stump, dist in road[now]:
            cost = (dist * 2) + d
            if cost < fox_dist[next_stump]:
                fox_dist[next_stump] = cost
                heapq.heappush(q, [cost, next_stump])


def wolf_dijkstra():
    q = [[0, 1, 0]]
    while q:
        d, now, state = heapq.heappop(q)
        if wolf_dist[now][state] < d:
            continue

        for next_stump, dist in road[now]:
            cost = (dist * wolf_speed[state]) + d
            next_state = 1 - state
            if cost < wolf_dist[next_stump][next_state]:
                wolf_dist[next_stump][next_state] = cost
                heapq.heappush(q, [cost, next_stump, next_state])


n, m = map(int, input().split())
road = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, d = map(int, input().split())
    road[a].append([b, d])
    road[b].append([a, d])

fox_dist = [float('inf')] * (n + 1)
wolf_dist = [[float('inf')] * 2 for _ in range(n + 1)]
wolf_speed = [1, 4]
ans = 0

fox_dijkstra()
wolf_dijkstra()

for i in range(2, n + 1):
    if fox_dist[i] < min(wolf_dist[i]):
        ans += 1

print(ans)
