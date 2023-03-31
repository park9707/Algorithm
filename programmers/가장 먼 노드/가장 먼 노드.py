from collections import deque, defaultdict


def solution(n, edge):
    maps = [[] for _ in range(n + 1)]
    for a, b in edge:
        maps[a].append(b)
        maps[b].append(a)

    arr = defaultdict(list)
    visited = [-1] * (n + 1)
    visited[1] = 0
    q = deque([1])

    while q:
        num = q.popleft()
        for i in maps[num]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[num] + 1
                arr[visited[i]].append(i)

    return len(arr[len(arr)])
