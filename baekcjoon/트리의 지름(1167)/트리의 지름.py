import sys
input = sys.stdin.readline

v = int(input().rstrip())
wire = [[] for _ in range(v + 1)]

for _ in range(v):
    temp = list(map(int, input().rstrip().split()))
    start = temp[0]
    for i in range(1, len(temp) - 1, 2):
        a, b = temp[i], temp[i + 1]
        wire[start].append((a, b))


def dfs(node):
    for next_node, w in wire[node]:
        if dist[next_node] == -1:
            dist[next_node] = dist[node] + w
            dfs(next_node)


dist = [-1] * (v + 1)
dist[1] = 0
dfs(1)

n = dist.index(max(dist))
dist = [-1] * (v + 1)
dist[n] = 0
dfs(n)

print(max(dist))
