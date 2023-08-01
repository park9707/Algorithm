import math


def solution(r1, r2):
    answer = 0

    for i in range(1, r2 + 1):
        high_r1 = math.sqrt(r2 ** 2 - i ** 2)
        high_r2 = 0 if i > r1 else math.sqrt(r1 ** 2 - i ** 2)
        answer += math.floor(high_r1) - math.ceil(high_r2) + 1

    return answer * 4
