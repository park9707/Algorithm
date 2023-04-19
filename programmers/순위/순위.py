from collections import defaultdict


def solution(n, results):
    answer = 0
    w_player = defaultdict(set)
    l_player = defaultdict(set)

    def w_dfs(w):
        visited[w] = True

        if l_player[w] == '':
            return

        for i in l_player[w]:
            if not visited[i]:
                w_player[i].update(w_player[winner])
                w_dfs(i)

    def l_dfs(l):
        visited[l] = True

        if w_player[l] == '':
            return

        for i in w_player[l]:
            if not visited[i]:
                l_player[i].update(l_player[loser])
                l_dfs(i)

    for winner, loser in results:
        visited = [False] * (n + 1)
        l_player[loser].add(winner)
        l_player[loser].update(l_player[winner])
        w_player[winner].add(loser)
        w_player[winner].update(w_player[loser])
        w_dfs(winner)
        l_dfs(loser)

    for i in range(1, n+1):
        if len(l_player[i]) + len(w_player[i]) == n-1:
            answer += 1

    return answer
