def solution(n, tops):
    dp = [1] * (2 * n + 2)

    for i in range(2, 2 * n + 2):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

        if i % 2 == 0 and tops[i // 2 - 1]:
            dp[i] += dp[i - 1]

    return dp[-1]