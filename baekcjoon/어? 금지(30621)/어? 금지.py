import sys
input = sys.stdin.readline

N = int(input())
t = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [0] * N
dp[0] = c[0]

for i in range(1, N):
    if t[i] == b[i]:
        dp[i] = max(dp[i-1], c[i])
        continue
    left = 0
    right = i
    num = t[i] - b[i]
    while left <= right:
        mid = (left + right) // 2
        if t[mid] < num:
            left = mid + 1
        elif t[mid] > num:
            right = mid - 1
        else:
            left = mid
            break

    dp[i] = max(dp[i-1], dp[left-1] + c[i])

print(dp[-1])