import sys
sys.setrecursionlimit(10**6)

def dfs(idx, a):
    global visited, graph, cnt
    visited[idx] = True

    for i in graph[idx]:
        if not visited[i]:
            tmp_num = dfs(i, a)
            cnt += abs(tmp_num)
            a[idx] += tmp_num

    return a[idx]


def solution(a, edges):
    if sum(a) != 0:
        return -1
    global graph, visited, cnt

    n = len(a)
    graph = [[] for _ in range(n)]
    visited = [False] * n

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    cnt = 0
    dfs(0, a)
    return cnt
