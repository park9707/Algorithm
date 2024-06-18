import sys, heapq
input = sys.stdin.readline


def dijkstra(start):
    graph = [[] for _ in range(n + 1)]
    for j in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])
    dist = [float('inf')] * (n + 1)
    q = [[0, start]]
    while q:
        t, com = heapq.heappop(q)
        if dist[com] < t:
            continue

        for next_com, s in graph[com]:
            cost = t + s
            if dist[next_com] > cost:
                dist[next_com] = cost
                heapq.heappush(q, [cost, next_com])
    dist[start] = 0
    ans = cnt = 0
    for i in range(1, n + 1):
        if dist[i] != float('inf'):
            ans = max(ans, dist[i])
            cnt += 1
    print(cnt, ans)


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    dijkstra(c)
