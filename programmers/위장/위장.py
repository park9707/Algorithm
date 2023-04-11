from collections import Counter


def solution(clothes):
    answer = 1
    arr = Counter([clothe for name, clothe in clothes])

    for i in arr:
        answer *= (arr[i]+1)

    return answer-1
