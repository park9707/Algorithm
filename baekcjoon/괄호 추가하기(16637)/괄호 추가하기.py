import sys
input = sys.stdin.readline

n = int(input())
data = input().rstrip()
result = float('-inf')


def operator(num1, num2, op):
    num2 = int(num2)
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2


def dfs(idx, value):
    if idx == n:
        global result
        result = max(result, value)
        return

    if idx + 3 < n:
        dfs(idx + 4, operator(value, operator(int(data[idx + 1]), data[idx + 3], data[idx + 2]), data[idx]))

    dfs(idx + 2, operator(value, data[idx + 1], data[idx]))


dfs(1, int(data[0]))

print(result)