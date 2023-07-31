def solution(n):
    dp = [3, 11]
    for i in range(2, n//2):
        dp.append((dp[i-1] * 4 - dp[i-2]) % 1000000007)
    return dp[-1]
