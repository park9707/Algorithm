import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    nums.sort()
    for i in range(n - 1):
        if nums[i] == nums[i + 1][:len(nums[i])]:
            print('NO')
            break
    else:
        print('YES')