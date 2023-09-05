import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

l = r = 0
num = nums[0]
answer = float('inf')

while l <= r:
    if num < s:
        r += 1
        if r == n:
            break
        num += nums[r]
    else:
        num -= nums[l]
        l += 1
        if num < s:
            answer = min(answer, r - l + 2)

print(answer if answer != float('inf') else 0)
