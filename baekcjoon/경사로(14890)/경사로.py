import sys
input = sys.stdin.readline

n, l = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
cnt = 0


def check_row(i):
    h = maps[i][0]
    cnt = 1
    for j in range(1, n):
        tmp = maps[i][j]
        if tmp == h:
            cnt += 1

        elif tmp == h + 1:
            if cnt >= l and not stair[i][j - l]:
                h = tmp
                cnt = 1
            else:
                return 0

        elif tmp + 1 == h:
            if j + l - 1 < n:
                stair[i][j] = 1
                for k in range(j + 1, j + l):
                    stair[i][k] = 1
                    if tmp != maps[i][k]:
                        return 0
                cnt = 1
                h = tmp
            else:
                return 0
        else:
            return 0
    return 1


def check_col(i):
    h = maps[0][i]
    cnt = 1
    for j in range(1, n):
        tmp = maps[j][i]
        if tmp == h:
            cnt += 1

        elif tmp == h + 1:
            if cnt >= l and not stair[j - l][i]:
                h = maps[j][i]
                cnt = 1
            else:
                return 0

        elif tmp + 1 == h:
            if j + l - 1 < n:
                stair[j][i] = 1
                for k in range(j + 1, j + l):
                    stair[k][i] = 1
                    if tmp != maps[k][i]:
                        return 0
                cnt = 1
                h = tmp
            else:
                return 0
        else:
            return 0
    return 1


stair = [[0] * n for _ in range(n)]
for i in range(n):
    cnt += check_row(i)

stair = [[0] * n for _ in range(n)]
for i in range(n):
    cnt += check_col(i)

print(cnt)
