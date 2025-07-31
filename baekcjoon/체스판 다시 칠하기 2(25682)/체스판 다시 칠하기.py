import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().rstrip().replace('B', '1').replace('W', '0'))) for _ in range(n)]
board_1 = [[0] * (m+1) for _ in range(n+1)]
board_2 = [[0] * (m+1) for _ in range(n+1)]
board_1[0][0] = 1

for i in range(n):
    for j in range(m):
        if (i + j) % 2:
            board_1[i][j] = board[i][j] + board_1[i-1][j] + board_1[i][j-1] - board_1[i-1][j-1]
            board_2[i][j] = ((i + 1) * (j + 1)) - board_1[i][j]
        else:
            board_2[i][j] = board[i][j] + board_2[i - 1][j] + board_2[i][j - 1] - board_2[i - 1][j - 1]
            board_1[i][j] = ((i + 1) * (j + 1)) - board_2[i][j]

ans = float('inf')
for i in range(n - k + 1):
    for j in range(m - k + 1):
        temp_b = board_1[i+k-1][j+k-1] - board_1[i-1][j+k-1] - board_1[i+k-1][j-1] + board_1[i-1][j-1]
        temp_w = board_2[i+k-1][j+k-1] - board_2[i-1][j+k-1] - board_2[i+k-1][j-1] + board_2[i-1][j-1]
        ans = min(ans, temp_b, temp_w)

print(ans)