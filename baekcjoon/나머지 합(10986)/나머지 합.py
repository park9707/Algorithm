import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
v = 0
numRemainder = [0] * M

for i in range(N):
    v += nums[i]
    numRemainder[v % M] += 1

ans = numRemainder[0]

for i in numRemainder:
    ans += i * (i - 1) // 2

print(ans)