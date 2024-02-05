import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
dp[1], _ = map(int, input().split())

for i in range(2, N + 1):
    t, indegree, *G = list(map(int, input().split()))
    dp[i] = t + (max([dp[j] for j in G]) if indegree else 0)

print(max(dp))
