def conv(num, p):
    n = ''
    while num > 0:
        num, r = divmod(num, p)
        n += str(r)

    if not n:
        return '0'
    return n[::-1]


def cal(a, op, b):
    if op == '+':
        num = a + b
    else:
        num = a - b
    return num


def solution(expressions):
    max_n = 0
    ex = []
    result = []
    for e in expressions:
        e = list(e.split())
        for i in [0, 2]:
            for c in e[i]:
                max_n = max(max_n, int(c))

        if e[4] == 'X':
            result.append(e)
        else:
            for c in e[4]:
                max_n = max(max_n, int(c))
                ex.append(e)

    candidate = list(range(max_n + 1, 10))

    for e in ex:
        new_cand = []
        for c in candidate:
            res = cal(int(e[0], c), e[1], int(e[2], c))
            if e[4] == conv(res, c):
                new_cand.append(c)

        candidate = new_cand

    for r in result:
        ans = set()
        for c in candidate:
            res = cal(int(r[0], c), r[1], int(r[2], c))
            ans.add(conv(res, c))

        if len(ans) == 1:
            r[4] = ans.pop()
        else:
            r[4] = '?'
    return [' '.join(r) for r in result]