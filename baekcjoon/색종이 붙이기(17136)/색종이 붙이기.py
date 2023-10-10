import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

board = []
cnt = 0
for _ in range(10):
    temp = list(map(int, input().rstrip().split()))
    cnt += temp.count(1)
    board.append(temp)
if cnt == 0:
    print(0)
    exit(0)
elif cnt == 100:
    print(4)
    exit(0)
confetti = [5] * 5
score = [1, 4, 9, 16, 25]
ans = float('inf')


def check(x, y, k):
    for i in range(x, x + k + 1):
        for j in range(y, y + k + 1):
            if board[i][j] == 0:
                return False
    return True


def toggle(x, y, k, n):
    for i in range(x, x + k + 1):
        for j in range(y, y + k + 1):
            board[i][j] = n


def backtracking(x, y, c, remain_cnt):
    global confetti
    if remain_cnt == 0:
        global ans
        ans = min(ans, c)
        return
    if x >= 10:
        return
    elif y >= 10:
        backtracking(x + 1, 0, c, remain_cnt)
    elif board[x][y] != 0:
        is_ex = False
        for k in range(5):
            if confetti[k] == 0:
                continue
            if 10 <= x + k or 10 <= y + k:
                continue

            if check(x, y, k):
                is_ex = True
                toggle(x, y, k, 0)
                confetti[k] -= 1
                backtracking(x, y + 1, c + 1, remain_cnt - score[k])
                confetti[k] += 1
                toggle(x, y, k, 1)

        if not is_ex:
            return
    else:
        backtracking(x, y + 1, c, remain_cnt)


backtracking(0, 0, 0, cnt)
print(ans if ans != float('inf') else -1)
