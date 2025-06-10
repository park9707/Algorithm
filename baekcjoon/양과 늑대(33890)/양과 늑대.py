import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
sheep = list(map(int, input().split()))
wolf = list(map(int, input().split()))
ans = 0

sheep.sort()
l, r = 0, n - 1
left_temp = []
right_temp = -1
while l < r:
    while sheep[l] + sheep[r] <= k and l < r:
        left_temp.append(sheep[l])
        l += 1

    if left_temp:
        left_temp.pop()
    else:
        right_temp = sheep[r]
    ans += 1
    r -= 1

if l == r:
    left_temp.append(sheep[l])

ans += len(left_temp) // 2
if right_temp != -1 and len(left_temp) % 2 == 0:
    ans -= 1
elif len(left_temp) % 2 == 1:
    right_temp = left_temp[0]

if right_temp != -1:
    wolf.append(right_temp)

wolf.sort()
l, r = 0, len(wolf) - 1
while l < r:
    if wolf[l] + wolf[r] <= k:
        l += 1
    r -= 1
    ans += 1

if l == r:
    ans += 1

print(ans)