import sys
input = sys.stdin.readline

n = int(input())


def hanoi(n, start, target, other):
    if n == 0:
        return
    else:
        hanoi(n - 1, start, other, target)
        print(start, target)
        hanoi(n - 1, other, target, start)


print(2 ** n - 1)
hanoi(n, 1, 3, 2)