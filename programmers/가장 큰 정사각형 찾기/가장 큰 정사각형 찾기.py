def solution(board):
    max_n = 0
    dp = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):
            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

                max_n = max(max_n, dp[i][j])
    return max_n ** 2