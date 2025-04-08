import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
if n <= 1:
    print('A')
elif n == 2:
    print(nums[1]) if nums[0] == nums[1] else print('A')
else:
    a = 0 if nums[0] == nums[1] else (nums[2] - nums[1]) // (nums[1] - nums[0])
    b = nums[1] - (nums[0] * a)
    for i in range(n - 1):
        if nums[i] * a + b != nums[i + 1]:
            print('B')
            exit()

    print(nums[-1] * a + b)