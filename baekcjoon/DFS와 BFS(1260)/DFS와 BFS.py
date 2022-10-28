from collections import deque

N, M, V = map(int, input().split())

matrix = [[False] * (N+1) for _ in range(N+1)]

visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = True

def dfs(V):
    visited[V] = True
    print(V, end=" ")

    for i in range(1, N+1):
        if not visited[i] and matrix[V][i]:
            dfs(i)

def bfs(V):
    queue = deque([V])
    visited[V] = False

    while queue:
        V = queue.popleft()
        print(V, end=" ")

        for i in range(1, N+1):
            if visited[i] and matrix[V][i]:
                visited[i] = False
                queue.append(i)

dfs(V)
print()
bfs(V)
