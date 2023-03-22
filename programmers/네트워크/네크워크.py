def solution(n, computers):
    answer = 0

    def dfs(c):
        computers[c][c] = 0

        for i in range(n):
            if computers[c][i] == 1:
                computers[c][i] = 0
                dfs(i)

    for i in range(n):
        if computers[i][i] == 1:
            dfs(i)
            answer += 1

    return answer
