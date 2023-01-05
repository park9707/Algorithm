from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    target = {}
    for i in range(len(want)):
        target[want[i]] = number[i]

    for i in range(len(discount) - 9):
        items = defaultdict(int)

        for j in range(i, i + 10):
            items[discount[j]] += 1

        if items == target:
            answer += 1

    return answer