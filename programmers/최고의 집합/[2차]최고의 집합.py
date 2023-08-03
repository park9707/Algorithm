def solution(n, s):
    if s < n:
        return [-1]
    remainder = s % n
    if remainder == 0:
        return [s // n] * n
    return [s // n] * (n - remainder) + [s // n + 1] * remainder
