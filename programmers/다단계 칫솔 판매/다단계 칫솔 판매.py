from collections import defaultdict


def solution(enroll, referral, seller, amount):
    m = defaultdict(int)
    wire = defaultdict()

    for e, r in zip(enroll, referral):
        wire[e] = r

    def dfs(name, money):
        if money < 1:
            return

        m[name] += money - money // 10

        if wire[name] == '-':
            return

        dfs(wire[name], money // 10)

    for s, a in zip(seller, amount):
        sell = 100 * a
        m[s] += sell - sell // 10
        if wire[s] != '-':
            dfs(wire[s], sell // 10)

    return [m[name] for name in enroll]
