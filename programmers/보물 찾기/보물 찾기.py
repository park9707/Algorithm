def solution(depth, money, excavate):
    n = len(depth)
    depth = [0] + depth
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    idx = [[0] * (n + 2) for _ in range(n + 2)]

    for scope in range(1, n + 1):
        for left in range(1, n - scope + 2):
            right = left + scope - 1
            best_cost = float('inf')
            best_idx = -1

            for i in range(left, right + 1):
                cost = depth[i] + max(dp[left][i - 1], dp[i + 1][right])

                if best_cost > cost:
                    best_cost = cost
                    best_idx = i

            dp[left][right] = best_cost
            idx[left][right] = best_idx

    left, right = 1, n

    while left <= right:
        col = idx[left][right]
        result = excavate(col)

        if result == 0:
            return col
        elif result == -1:
            right = col - 1
        else:
            left = col + 1