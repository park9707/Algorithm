import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(int(input()))
    exit()
nums = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0
i = 0
while i < n - 1 and nums[i + 1] > 1:
    ans += (nums[i] * nums[i + 1])
    i += 2

while i < n - 1 and nums[i] > 0:
    ans += nums[i]
    i += 1

z = 0
while i < n - 1 and nums[i] == 0:
    z += 1
    i += 1

if (n - i) % 2 == 1:
    if z == 0:
        ans += nums[i]
    i += 1

for j in range(i, n, 2):
    ans += (nums[j] * nums[j + 1])

print(ans)