import sys
input = sys.stdin.readline


def bellman_ford(start):
    node[start] = 0
    for i in range(N-1):
        for j in range(M):
            cur_node, next_node, cost = wire[j]
            node[next_node] = min(node[next_node], node[cur_node] + cost)

    for j in range(M):
        cur_node, next_node, cost = wire[j]
        if node[next_node] > node[cur_node] + cost:
            return False
    return True


N, M = map(int, input().split())
node = [float("inf")] * (N + 1)
wire = [list(map(int, input().split())) for _ in range(M)]

if not bellman_ford(1):
    print(-1)
else:
    for i in range(2, N + 1):
        print(node[i] if node[i] != float("inf") else -1)