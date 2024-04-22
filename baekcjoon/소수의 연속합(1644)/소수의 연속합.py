import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(0)
    exit()
arr = [True] * (N + 1)
prime_nums = [0]
for i in range(2, int(N ** 0.5) + 1):
    if arr[i]:
        for j in range(i + i, N + 1, i):
            arr[j] = False

for i in range(2, N + 1):
    if arr[i]:
        prime_nums.append(i)

l = r = len(prime_nums) - 1
num = prime_nums[l]
ans = 0

while 0 < l:
    if num < N:
        l -= 1
        num += prime_nums[l]
    elif num > N:
        num -= prime_nums[r]
        r -= 1
    else:
        ans += 1
        l -= 1
        num += prime_nums[l]

print(ans)