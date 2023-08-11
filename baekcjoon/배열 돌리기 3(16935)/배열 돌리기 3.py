import sys
input = sys.stdin.readline


def op_1(arr):
    return arr[::-1]


def op_2(arr):
    temp = []
    for i in arr:
        temp.append(i[::-1])
    return temp


def op_3(arr, n, m):
    temp = []
    for i in range(m):
        a = []
        for j in range(n-1, -1, -1):
            a.append(arr[j][i])
        temp.append(a)
    return temp


def op_4(arr, n, m):
    temp = []
    for i in range(m-1, -1, -1):
        a = []
        for j in range(n):
            a.append(arr[j][i])
        temp.append(a)
    return temp


def op_5_6(arr, n, m, num):
    temp = []
    a, b = [], []
    for i in range(n):
        a.append(arr[i][:m//2])
        b.append(arr[i][m//2:])
        if i == n//2-1:
            temp.append(a)
            temp.append(b)
            a, b = [], []
    temp.append(b)
    temp.append(a)
    result = []
    if num == 5:
        result.extend(rotate(temp, 3, 0))
        result.extend(rotate(temp, 2, 1))
    elif num == 6:
        result.extend(rotate(temp, 1, 2))
        result.extend(rotate(temp, 0, 3))
    return result


def rotate(arr_piece, left, right):
    tmp = []
    for i in range(len(arr_piece[0])):
        tmp.append(arr_piece[left][i] + arr_piece[right][i])
    return tmp


n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
nums = list(map(int, input().split()))
for num in nums:
    if num == 1:
        arr = op_1(arr)
    elif num == 2:
        arr = op_2(arr)
    elif num == 3:
        arr = op_3(arr, len(arr), len(arr[0]))
    elif num == 4:
        arr = op_4(arr, len(arr), len(arr[0]))
    else:
        arr = op_5_6(arr, len(arr), len(arr[0]), num)

for a in arr:
    print(' '.join(map(str, a)))
