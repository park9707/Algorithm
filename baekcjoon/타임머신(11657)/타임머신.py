import sys

input = sys.stdin.readline


def bellman_ford(start):
    node[start] = 0
    for _ in range(N - 1):
        for cur_node in range(1, N + 1):
            if node[cur_node] == float("inf"):
                continue

            for next_node, cost in wire[cur_node]:
                node[next_node] = min(node[next_node], node[cur_node] + cost)

    for cur_node in range(1, N + 1):
        for next_node, cost in wire[cur_node]:
            if node[next_node] > node[cur_node] + cost:
                return False
    return True


N, M = map(int, input().split())
node = [float("inf")] * (N + 1)
wire = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    wire[a].append([b, c])

if not bellman_ford(1):
    print(-1)
else:
    for i in range(2, N + 1):
        print(node[i] if node[i] != float("inf") else -1)