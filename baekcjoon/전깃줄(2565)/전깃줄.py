import sys
input = sys.stdin.readline

n = int(input())
arr = []
dp = [1] * n

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort()

for i in range(1, n):
    p = arr[i][1]
    for j in range(i):
        if arr[j][1] < p:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))