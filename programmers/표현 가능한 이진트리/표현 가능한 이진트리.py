import math


def check(n, left, right):
    dif = (right - left) // 2
    mid = left + dif

    if dif <= 1:
        if n[mid] == '1' or '1' not in n[left:right+1]:
            return True
        return False

    if n[mid] == '0':
        for i in range(left, right + 1):
            if n[i] == '1':
                return False
        return True
    else:
        if check(n, left, mid - 1):
            if check(n, mid + 1, right):
                return True
        return False


def solution(numbers):
    answer = []
    for num in numbers:
        b = format(num, 'b')
        length = len(b)
        n = 2 ** (int(math.log(length, 2)) + 1) - 1
        b = ('0' * (n - length)) + b

        if check(b, 0, len(b)-1):
            answer.append(1)
        else:
            answer.append(0)

    return answer
