import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def left(board):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            num = board[i][j]
            if num != 0:
                board[i][j] = 0
                if num == board[i][pointer]:
                    board[i][pointer] = num * 2
                    pointer += 1
                elif board[i][pointer] == 0:
                    board[i][pointer] = num
                else:
                    pointer += 1
                    board[i][pointer] = num

    return board


def right(board):
    for i in range(n):
        pointer = n-1
        for j in range(n-2, -1, -1):
            num = board[i][j]
            if num != 0:
                board[i][j] = 0
                if num == board[i][pointer]:
                    board[i][pointer] = num * 2
                    pointer -= 1
                elif board[i][pointer] == 0:
                    board[i][pointer] = num
                else:
                    pointer -= 1
                    board[i][pointer] = num

    return board


def up(board):
    for j in range(n):
        pointer = 0
        for i in range(1, n):
            num = board[i][j]
            if num != 0:
                board[i][j] = 0
                if num == board[pointer][j]:
                    board[pointer][j] = num * 2
                    pointer += 1
                elif board[pointer][j] == 0:
                    board[pointer][j] = num
                else:
                    pointer += 1
                    board[pointer][j] = num

    return board


def down(board):
    for j in range(n):
        pointer = n-1
        for i in range(n-2, -1, -1):
            num = board[i][j]
            if num != 0:
                board[i][j] = 0
                if num == board[pointer][j]:
                    board[pointer][j] = num * 2
                    pointer -= 1
                elif board[pointer][j] == 0:
                    board[pointer][j] = num
                else:
                    pointer -= 1
                    board[pointer][j] = num

    return board


def dfs(board, cnt):
    if cnt == 5:
        return max(max(board, key=max))

    return max(dfs(up(deepcopy(board)), cnt+1), dfs(down(deepcopy(board)), cnt+1), dfs(left(deepcopy(board)), cnt+1), dfs(right(deepcopy(board)), cnt+1))

print(dfs(board, 0))
