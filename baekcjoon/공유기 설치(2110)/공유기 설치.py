import sys
input = sys.stdin.readline

n, c = map(int, input().rstrip().split())
houses = sorted([int(input().rstrip()) for _ in range(n)])
left = 1
right = (houses[-1] - houses[0]) // (c - 1)

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    temp = houses[0]
    for house in houses[1:]:
        if mid <= house - temp:
            temp = house
            cnt += 1

    if cnt < c:
        right = mid - 1
    else:
        left = mid + 1

print(right)
