import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    arr = [0] + list(map(int, input().split()))
    s = [0] * (k + 1)

    s[1] = arr[1]
    for i in range(2, k + 1):
        s[i] = s[i - 1] + arr[i]

    dp = [[0] * (k + 1) for _ in range(k + 1)]

    for n in range(2, k + 1):
        for i in range(1, k - n + 2):
            dp[i][i+n-1] = min(dp[i][j] + dp[j+1][i+n-1] for j in range(i, i+n-1)) + (s[i+n-1] - s[i-1])

    print(dp[1][k])