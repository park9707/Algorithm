def dfs(node, s, w, info, visited):
    global maps, answer
    visited[node].append(s)

    for i in maps[node]:
        if s not in visited[i]:
            if info[i] == 2:
                dfs(i, s, w, info, visited)
            elif info[i] == 0:
                info[i] = 2
                dfs(i, s + 1, w, info, visited)
                info[i] = 0
            elif info[i] == 1:
                if s > w + 1:
                    info[i] = 2
                    dfs(i, s, w + 1, info, visited)
                    info[i] = 1
    answer = max(answer, s)


def solution(info, edges):
    global maps, answer
    answer = 1
    n = len(info)
    maps = [[] * n for _ in range(n)]
    for a, b in edges:
        maps[a].append(b)
        maps[b].append(a)
    info[0] = 2

    for i in maps[0]:
        if info[i] == 0:
            info[i] = 2
            visited = [[] for _ in range(n)]
            visited[0].append(1)
            dfs(i, 2, 0, info, visited)
            info[i] = 0

    return answer
