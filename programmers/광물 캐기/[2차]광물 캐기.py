def solution(picks, minerals):
    answer = 0
    max_pick = sum(picks)
    n = len(minerals)
    dic = {"diamond": 0, "iron": 1, "stone": 2}
    m = [[0, 0, 0] for _ in range(max_pick + 1)]

    for i in range(1, min(max_pick * 5, n) + 1, 5):
        for j in range(i-1, min(n, i + 4)):
            mineral = minerals[j]
            m[i//5+1][dic[mineral]] += 1

    m.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

    i = 0
    for idx, pick in enumerate(picks):
        for k in range(i, min(n, i + pick)):
            a, b, c = m[k]
            a *= 5 ** idx
            if idx == 2:
                b *= 5
            answer += a + b + c
        i += pick

    return answer
