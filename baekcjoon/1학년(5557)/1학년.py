import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [0] * 21
dp[nums[0]] = 1
arr = {nums[0]}

for i in range(1, n - 1):
    new_dp = [0] * 21
    new_arr = set()
    for num in arr:
        num_plus = num + nums[i]
        num_minus = num - nums[i]
        if num_plus <= 20:
            new_dp[num_plus] += dp[num]
            new_arr.add(num_plus)
        if 0 <= num_minus:
            new_dp[num_minus] += dp[num]
            new_arr.add(num_minus)
    dp = new_dp
    arr = new_arr

print(dp[nums[-1]])