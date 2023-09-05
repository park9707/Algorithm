import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

l = r = 0
answer = []
num = nums[0]

while r < n:
    while s <= num:
        num -= nums[l]
        l += 1
        if s > num:
            answer.append(r - l + 2)
    while num < s:
        r += 1
        if r == n:
            break
        num += nums[r]

print(min(answer) if answer else 0)
