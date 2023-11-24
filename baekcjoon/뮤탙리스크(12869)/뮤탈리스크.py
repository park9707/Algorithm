import sys, itertools
input = sys.stdin.readline

n = int(input())
scv = list(map(int, input().split()))
scv += [0] * (3 - len(scv))
dp = [[[float('inf')] * 61 for _ in range(61)] for _ in range(61)]
damage = list(itertools.permutations((9, 3, 1)))
dp[scv[0]][scv[1]][scv[2]] = 0

for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] != float('inf'):
                for a, b, c in damage:
                    next_i = max(i - a, 0)
                    next_j = max(j - b, 0)
                    next_k = max(k - c, 0)
                    dp[next_i][next_j][next_k] = min(dp[next_i][next_j][next_k], dp[i][j][k] + 1)

print(dp[0][0][0])