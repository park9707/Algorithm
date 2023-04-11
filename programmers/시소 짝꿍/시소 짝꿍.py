from collections import Counter


def solution(weights):
    answer = 0
    count = Counter(weights)
    for i in count.values():
        if i > 1:
            answer += i * (i - 1) // 2

    for i in count:
        for check in (3/4, 2/4, 2/3):
            if i * check in count:
                answer += count[i] * count[i * check]
    return answer