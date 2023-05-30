import heapq


def solution(alp, cop, problems):
    problems += ([0, 0, 1, 0, 1], [0, 0, 0, 1, 1])
    alp_goal, cop_goal = max(i[0] for i in problems), max(i[1] for i in problems)
    dp = [[float("inf")] * (cop_goal + 1) for _ in range(alp_goal + 1)]
    q = []
    heapq.heappush(q, (0, alp, cop))
    dp[alp][cop] = 0

    while q[0][1] < alp_goal or q[0][2] < cop_goal:
        t, now_alp, now_cop = heapq.heappop(q)

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if now_alp < alp_req or now_cop < cop_req:
                continue
                
            sum_t = t + cost
            sum_alp, sum_cop = min(now_alp + alp_rwd, alp_goal), min(now_cop + cop_rwd, cop_goal)
            if sum_t < dp[sum_alp][sum_cop]:
                heapq.heappush(q, (sum_t, sum_alp, sum_cop))
                dp[sum_alp][sum_cop] = sum_t

    return q[0][0]