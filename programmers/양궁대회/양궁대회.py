from copy import deepcopy


def dfs(i, n, r, a):
    if n != 0:
        for j in range(i, -1, -1):
            r[10-j] += 1
            n -= 1

            if r[10-j] - a[10-j] < 2:
                dfs(j, n, r, a)

            r[10 - j] -= 1
            n += 1

    if n == 0:
        score = 0

        for k in range(11):
            if r[10-k] > a[10-k]:
                score += k
            elif a[10-k] != 0:
                score -= k
        if score > 0:
            answer.append([score, deepcopy(r)])


def solution(n, info):
    global answer
    answer = []
    dfs(10, n, [0 for _ in range(11)], info)
    answer.sort(key=lambda x: (x[0], x[1][::-1]), reverse=True)

    return answer[0][1] if answer else [-1]
