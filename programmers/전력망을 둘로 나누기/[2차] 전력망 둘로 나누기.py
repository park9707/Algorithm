def solution(n, wires):
    answer = float("inf")
    global cnt

    def dfs(n):
        global cnt
        cnt += 1
        visited[n] = True

        for i in maps[n]:
            if not visited[i]:
                dfs(i)

    for i in range(len(wires)):
        maps = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            maps[a].append(b)
            maps[b].append(a)

        tmp = []

        for k in range(1, n + 1):
            if not visited[k]:
                cnt = 0
                dfs(k)
                tmp.append(cnt)

        if len(tmp) > 1:
            answer = min(answer, abs(tmp[0] - tmp[1]))

    return answer