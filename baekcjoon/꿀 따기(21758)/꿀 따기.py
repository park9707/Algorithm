import sys
input = sys.stdin.readline

N = int(input())
prefix_sum = [0] * N
honeys = list(map(int, input().split()))

for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1] + honeys[i]
left_sum = prefix_sum[-2] + honeys[0]
ans = 0

for i in range(1, N-1):
    # (ans, 왼쪽 -> 오른쪽 끝, 오른쪽 -> 왼쪽 끝, 벌집이 i에 있을 때) 비교
    ans = max(ans,
              prefix_sum[-1] * 2 - prefix_sum[i-1] - honeys[i] * 2,
              left_sum + prefix_sum[-i-1] + honeys[0] - honeys[-i-1] * 2,
              prefix_sum[-2] + honeys[i])

print(ans)