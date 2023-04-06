def solution(picks, minerals):
    picks_n = sum(picks)
    max_m = picks_n * 5
    minerals = minerals[:max_m]
    d = picks[0]
    ir = picks[1]

    m = [[0, 0, 0] for _ in range(max_m // 5)]

    for i in range(max_m // 5):
        for mineral in minerals[i * 5:i * 5 + 5]:
            if mineral == 'diamond':
                m[i][0] += 1
            elif mineral == 'iron':
                m[i][1] += 1
            elif mineral == 'stone':
                m[i][2] += 1

    m.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

    answer = 0

    for i in range(d):
        answer += sum(m[i])
    for i in range(d, d + ir):
        answer += m[i][0] * 5 + m[i][1] + m[i][2]
    for i in range(d + ir, picks_n):
        answer += m[i][0] * 25 + m[i][1] * 5 + m[i][2]

    return answer
