from collections import defaultdict
from itertools import combinations
def solution(orders, course):
    answer = []
    length = 0
    for i in orders:
        length = max(length, len(i))

    for i in course[:len(course)]:
        if i > length:
            break
        dic = defaultdict(int)
        for j in orders:
            if len(j) < i:
                continue
            arr = list(combinations(sorted(j), i))
            for k in arr:
                k = sorted(k)
                dic[''.join(k)] += 1

        dic = sorted(dic.items(), key = lambda x:x[1], reverse = True)
        if dic[0][1] > 1:
            answer.append(dic[0][0])
            for k in dic[1:]:
                if k[1] == dic[0][1]:
                    answer.append(k[0])
                else:
                    break

    answer.sort(key = lambda x : x*10)
    return answer