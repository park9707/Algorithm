import sys
input = sys.stdin.readline

n = int(input())
nums = [(int(input()))]
ans = 0
for _ in range(n-1):
    num = int(input())
    while nums and nums[-1] <= num:
        nums.pop()
    nums.append(num)
    ans += len(nums) - 1

print(ans)