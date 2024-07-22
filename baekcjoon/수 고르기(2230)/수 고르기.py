import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted([int(input()) for _ in range(n)])
l, r = 0, 1
ans = float('inf')

while r < n:
    if nums[r] - nums[l] >= m:
        ans = min(ans, nums[r] - nums[l])
        l += 1
        if l >= r:
            r += 1
    else:
        r += 1

print(ans)