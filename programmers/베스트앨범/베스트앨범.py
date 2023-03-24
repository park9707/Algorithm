from collections import defaultdict


def solution(genres, plays):
    answer = []
    dic1 = defaultdict(int)
    dic2 = defaultdict(list)
    for i in range(len(genres)):
        dic1[genres[i]] += plays[i]
        dic2[genres[i]].append((plays[i], i))

    for k, v in sorted(dic1.items(), key=lambda x: x[1], reverse=True):
        for t, i in sorted(dic2[k], key=lambda x: x[0], reverse=True)[:2]:
            answer.append(i)
    return answer
