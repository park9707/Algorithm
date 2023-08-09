import sys
input = sys.stdin.readline

n = int(input())
stick = list(map(int, input().split()))
stick.sort()
q = int(input())
target = list(map(int, input().split()))
max_target = max(target)
dp = [0] * (max_target + 1)


def dfs(num):
    for i in range(num + num, max_target + 1, num):
        dp[i] += 1
        dfs(i)


for s in stick:
    dp[s] += 1
    dfs(s)

print(" ".join([str(dp[t]) for t in target]))
