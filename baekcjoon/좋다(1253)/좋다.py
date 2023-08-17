import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(map(int, input().split()))
cnt = 0

for i in range(n):
    left = 0
    right = n - 1
    target = nums[i]
    while left < right:
        num = nums[left] + nums[right]
        if num == target:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                cnt += 1
                break
        elif num < target:
            left += 1
        elif num > target:
            right -= 1
print(cnt)