from collections import Counter


def solution(weights):
    answer = 0
    dic = Counter(weights)
    for key in dic:
        v = dic[key]
        if v > 1:
            answer += v * (v - 1) // 2
        for i in (2/4, 3/4, 2/3):
            if key * i in dic:
                answer += dic[key * i] * v
    return answer
