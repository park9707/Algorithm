from itertools import combinations

def solution(relation):
    combi = []
    for i in range(1, len(relation[0])+1):
        combi.extend(combinations(range(len(relation[0])), i))

    arr = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        if len(tmp) == len(set(tmp)):
            for k in arr:
                if set(k).issubset(i):
                    break
            else:
                arr.append(i)

    return len(arr)