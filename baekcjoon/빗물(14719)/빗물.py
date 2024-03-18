import sys
input = sys.stdin.readline

_, W = map(int, input().split())
left_max = [0] * W
right_max = [0] * W
blocks = list(map(int, input().split()))
left_max[0] = blocks[0]
right_max[-1] = blocks[-1]
ans = 0

for i in range(1, W):
    left_max[i] = max(left_max[i-1], blocks[i])
    right_max[W-i-1] = max(right_max[W-i], blocks[W-i-1])

for i in range(1, W):
    ans += min(left_max[i], right_max[i]) - blocks[i]

print(ans)