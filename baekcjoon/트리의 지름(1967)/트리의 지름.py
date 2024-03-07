import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(node):
    visited[node] = True
    for next_node, weight in wire[node]:
        if not visited[next_node]:
            d[next_node] = d[node] + weight
            dfs(next_node)


n = int(input())
wire = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
d = [0] * (n + 1)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    wire[a].append([b, c])
    wire[b].append([a, c])

dfs(1)
node = d.index(max(d))
visited = [False] * (n + 1)
d[node] = 0
dfs(node)

print(max(d))