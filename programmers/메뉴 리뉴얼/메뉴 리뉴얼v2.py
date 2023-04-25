from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        combi = []
        for order in orders:
            combi.extend(combinations(sorted(order), c))
        most_order = Counter(combi).most_common()
        answer.extend(k for k, v in most_order if v > 1 and v == most_order[0][1])

    return [''.join(w) for w in sorted(answer)]
