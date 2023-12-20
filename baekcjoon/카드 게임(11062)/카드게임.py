import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]
    turn = True if N % 2 == 0 else False
    if not turn:
        for i in range(N):
            dp[i][i] = cards[i]

    for r in range(1, N):
        for l in range(N - r):
            if turn:
                dp[l][l + r] = max(dp[l + 1][l + r] + cards[l], dp[l][l + r - 1] + cards[l + r])
            else:
                dp[l][l + r] = min(dp[l + 1][l + r], dp[l][l + r - 1])

        turn = not turn

    print(dp[0][N - 1])