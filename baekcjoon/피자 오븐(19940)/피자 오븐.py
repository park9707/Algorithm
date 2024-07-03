import sys
input = sys.stdin.readline
# +60/+10/-10/+1/-1

T = int(input())
for _ in range(T):
    n = int(input())
    ans = [0 for _ in range(5)]
    a, b, c = n // 60, (n % 60) // 10, n % 10
    if c > 5:
        b += 1
        c -= 10
    if b > 3:
        a += 1
        b -= 6
    if b < 0 and c == 5:
        b += 1
        c -= 10

    ans[0] = a

    if b >= 0:
        ans[1] = b
    else:
        ans[2] = -b
    if c >= 0:
        ans[3] = c
    else:
        ans[4] = -c

    print(*ans)
