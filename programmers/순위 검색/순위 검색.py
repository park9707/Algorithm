import bisect, itertools, collections

def solution(info, query):
    inf = collections.defaultdict(list)
    case = list(itertools.product((True, False), repeat=4)) # 경우의 수 16가지
    for i in info:
        i = i.split()
        for c in case:
            key = ''.join([i[j] if c[j] else '-' for j in range(4)]) # inf로 나올 수 있는 16가지 경우의 수를 전부 저장
            inf[key].append(int(i[4])) # 조합을 키로 하여 점수를 담는다.

    for k in inf.keys():
        inf[k].sort() # 점수 정렬

    answers = []
    for q in query: # 쿼리를 하나씩 받아온다.
        l,_,o,_,c,_,f, p = q.split() # split해서 and를 버리고 나눠서 받는다.
        key = ''.join([l,o,c,f]) # 남은 조건을 한 단어로 합친다.
        idx = bisect.bisect_left(inf[key], int(p)) # 점수 조건을 만족하는 첫 값의 인덱스
        answers.append(len(inf[key]) - idx) # 조건에 맞지 않는 요소의 개수를 뺌

    return answers

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))