from collections import deque


def solution(lines):
    answer = 1
    tmp = []
    for line in lines:
        d, t, dt = line.split()
        t = float(t[:2]) * 3600 + float(t[3:5]) * 60 + float(t[6:8]) + float(t[8:])
        nt = float(dt[:-1])
        tmp.append([round(t - nt + 0.001, 3), 1])
        tmp.append([round(t + 0.999, 3), 2])

    q = deque(sorted(tmp))
    n = 0

    while q:
        a = q.popleft()
        if a[1] == 1:
            n += 1
        else:
            n -= 1

        answer = max(answer, n)

    return answer
