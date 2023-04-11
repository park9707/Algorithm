def solution(progresses, speeds):
    answer = []
    i = 0
    d = 0
    while i < len(progresses):
        remain = 100 - progresses[i] - (speeds[i] * d)
        d += remain // speeds[i]
        if remain % speeds[i] != 0:
            d += 1
        i += 1
        cnt = 1

        while i < len(progresses) and 100 - progresses[i] <= speeds[i] * d:
            cnt += 1
            i += 1

        answer.append(cnt)

    return answer
