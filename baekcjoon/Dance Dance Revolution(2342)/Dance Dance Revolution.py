import sys
input = sys.stdin.readline

move = [[2, 2, 2, 2, 2], [0, 1, 3, 4, 3], [0, 3, 1, 3, 4], [0, 4, 3, 1, 3], [0, 3, 4, 3, 1]]
instruction = map(int, input()[:-2].split())
dp, a = [float('inf')] * 5, 0
dp[0] = 0
for i in instruction:
    nums = [dp[j] + move[j][i] for j in range(5)]
    dp[a] = min(nums)
    for k in range(5):
        if k == a:
            continue
        dp[k] += move[a][i]
    a = i

print(min(dp))
