def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(n):
        nonlocal answer, dungeons, k
        for i in range(len(dungeons)):
            if not visited[i]:
                if k >= dungeons[i][0]:
                    visited[i] = True
                    k -= dungeons[i][1]
                    dfs(n+1)
                    visited[i] = False
                    k += dungeons[i][1]

        answer = max(answer, n)

    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            visited[i] = True
            k -= dungeons[i][1]
            dfs(1)
            visited[i] = False
            k += dungeons[i][1]

    return answer
