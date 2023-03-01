from sys import stdin
input = stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

dp = [list([0] * n) for _ in range(n)]

for i in range(n):  # 길이가 1이면 무조건 팰린드롬
    dp[i][i] = 1

for i in range(n - 1):  # 길이가 2
    if nums[i] == nums[i + 1]:  # 팰린드롬이라면 1 저장
        dp[i][i + 1] = 1

for i in range(2, n):  # 범위 3자리 이상 비교
    for start in range(n-i):  # 0 ~ n-i까지 비교
        end = start + i  # 시작과 i 범위 뒤의 숫자 비교
        if nums[start] == nums[end] and dp[start + 1][end - 1] == 1:  # 시작 숫자와 끝 숫자가 같고, 그 사이가 팰린드롬이라면
            dp[start][end] = 1

m = int(input().rstrip())
for _ in range(m):
    s, e = map(int, input().rstrip().split())
    print(dp[s-1][e-1])