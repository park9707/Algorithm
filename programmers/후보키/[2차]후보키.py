from itertools import combinations


def solution(relation):
    answer = []
    arr = list(range(len(relation[0])))
    n = len(relation)
    for i in range(1, len(arr) + 1):
        for combi in combinations(arr, i):
            tmp = [tuple(col[key] for key in combi) for col in relation]
            if len(set(tmp)) == n:
                for num in answer:
                    if set(num).issubset(combi):
                        break
                else:
                    answer.append(combi)
    return len(answer)
