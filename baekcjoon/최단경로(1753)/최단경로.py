import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
board = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    board[a].append([c, b])

dist = [float('inf')] * (v + 1)
dist[k] = 0
q = []
heapq.heappush(q, [0, k])

while q:
    d, node = heapq.heappop(q)

    if dist[node] < d:
        continue

    for next_d, next_node in board[node]:
        temp = d + next_d
        if temp < dist[next_node]:
            dist[next_node] = temp
            heapq.heappush(q, [temp, next_node])

for i in range(1, v + 1):
    print(dist[i] if dist[i] != float('inf') else 'INF')
