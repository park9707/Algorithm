def solution(n, s):
    if n > s:
        return [-1]
    elif s % n == 0:
        return [(s//n)]*n
    else:
        a = s % n
        return [(s//n)] * (n-a) + [(s//n)+1] * a
