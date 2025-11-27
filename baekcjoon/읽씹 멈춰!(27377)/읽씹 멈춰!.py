import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s, t = map(int, input().split())
    ans = 0
    while n > 0:
        if n % 2 == 1:
            n -= 1
            ans += s
        else:
            n //= 2
            ans += min(n * s, t)
    print(ans)