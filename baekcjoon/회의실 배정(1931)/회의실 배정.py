import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x: (x[1], x[0]))
ans = 0
current_t = -1
for start_t, end_t in time:
    if start_t >= current_t:
        current_t = end_t
        ans += 1

print(ans)
