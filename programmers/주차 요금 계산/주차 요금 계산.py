from collections import defaultdict


def solution(fees, records):
    answer = []
    t = defaultdict(int)
    dic = defaultdict(list)

    for record in records:
        time, i, inout = record.split()
        time = int(time[:2]) * 60 + int(time[3:])
        if inout == 'IN':
            dic[i].append(time)
        else:
            t[i] += time - dic[i].pop()

    for i in dic:
        if dic[i]:
            time = (23 * 60) + 59
            enter_time = dic[i].pop()
            t[i] += time - enter_time

    for car in sorted(t):
        time = t[car] - fees[0]
        if time > 0:
            cost = fees[1] + ((time // fees[2]) * fees[3])
            if time % fees[2] != 0:
                cost += fees[3]
            answer.append(cost)
        else:
            answer.append(fees[1])
    return answer
