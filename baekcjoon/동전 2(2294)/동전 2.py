n, k = map(int, input().split())

coins = set([int(input()) for _ in range(n)])

dp = [0] + ([float("inf")] * k)

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i - coin] + 1, dp[i])

if dp[k] > k:
    print("-1")
else:
    print(dp[k])