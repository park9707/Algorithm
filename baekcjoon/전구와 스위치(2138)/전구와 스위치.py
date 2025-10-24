import sys
input = sys.stdin.readline


def press(bulbs):
    cnt = 0
    for i in range(1, n):
        if bulbs[i - 1] != target[i - 1]:
            cnt += 1
            a, b = i - 1, min(i + 2, n)
            for j in range(a, b):
                bulbs[j] ^= 1

    return cnt if bulbs[-1] == target[-1] else n + 1


n = int(input())
now = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))
ans = [press(now[:])]

now[0] ^= 1
now[1] ^= 1

ans.append(press(now) + 1)

print(min(ans) if ans[0] <= n or ans[1] <= n else -1)