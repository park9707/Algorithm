import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(n):
    global result
    for node in graph[n]:
        if visited[node] == -1:
            if visited[n] == 1:
                visited[node] = 2
            if visited[n] == 2:
                visited[node] = 1
            dfs(node)
        else:
            if visited[n] == visited[node]:
                result = False
                return


k = int(input().rstrip())

for _ in range(k):
    v, e = map(int, input().rstrip().split())
    visited = [-1] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    result = True

    for i in range(1, v + 1):
        if visited[i] == -1:
            visited[i] = 1
            dfs(i)
            if result == False:
                print("NO")
                break
    else:
        print("YES")
