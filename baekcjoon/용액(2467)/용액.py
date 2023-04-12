import sys

input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

l, r = 0, n - 1
dif = sys.maxsize
x, y = arr[l], arr[r]

while l < r:
    tmp = arr[l] + arr[r]

    if abs(tmp) < dif:
        dif = abs(tmp)
        x = arr[l]
        y = arr[r]

    if tmp < 0:
        l += 1
    elif tmp > 0:
        r -= 1
    else:
        break

print(x, y)
