def solution(enroll, referral, seller, amount):
    node, money = {}, {e: 0 for e in enroll}

    for e, r in zip(enroll, referral):
        node[e] = r

    for s, a in zip(seller, amount):
        sell = a * 100
        m = sell // 10
        money[s] += sell - m
        refer = node[s]

        while refer != '-':
            if m == 0:
                break
            money[refer] += m - m // 10
            m //= 10
            refer = node[refer]

    return [money[e] for e in enroll]