from sys import stdin

input = stdin.readline
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

left, right = 1, max(lines)

while left <= right:
    mid = (left + right) // 2
    a = 0
    for line in lines:
        a += line // mid

        if a >= n:
            break

    if a >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)
