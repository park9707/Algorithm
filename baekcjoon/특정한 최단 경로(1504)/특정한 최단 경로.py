import sys, heapq
input = sys.stdin.readline

n, e = map(int, input().split())
wire = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    wire[a].append([c, b])
    wire[b].append([c, a])

v1, v2 = list(map(int, input().split()))


def dijkstra(start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    q = [[0, start]]
    while q:
        d, current_location = heapq.heappop(q)

        if dist[current_location] < d:
            continue

        for next_d, next_location in wire[current_location]:
            new_d = d + next_d
            if dist[next_location] < new_d:
                continue

            dist[next_location] = new_d
            heapq.heappush(q, [new_d, next_location])
    return dist


goal_dist1 = dijkstra(v1)
goal_dist2 = dijkstra(v2)
answer = min(goal_dist1[1] + goal_dist1[v2] + goal_dist2[n], goal_dist2[1] + goal_dist2[v1] + goal_dist1[n])
print(answer if answer != float('inf') else -1)
