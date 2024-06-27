import sys
input = sys.stdin.readline


def check(l, r, n):
    if n >= 2 or l >= r:
        return n
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if n == 0:
                if r - l < 2:
                    return 1
                elif check(l + 1, r, n + 1) == 1 or check(l, r - 1, n + 1) == 1:
                    return 1
            return 2
    return n


for _ in range(int(input())):
    s = input().rstrip()
    print(check(0, len(s) - 1, 0))
