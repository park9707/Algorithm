import sys
input = sys.stdin.readline

n, l = map(int, input().split())
puddle = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
end = -1
ans = 0

for left, right in puddle:
    if left < end:
        left = end
    length = right - left
    ans += length // l
    if length % l:
        ans += 1
        end = right + (l - (length % l))
    else:
        end = right

print(ans)