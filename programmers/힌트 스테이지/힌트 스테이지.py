def solution(cost, hint):
    n = len(cost)
    arr = [[0] * (n + 1)]

    for i in range(n):
        new_arr = []

        for stage in arr:
            base = stage[:]
            h = base[i + 1]
            base[0] += cost[i][min(h, len(cost[0]) - 1)]
            new_arr.append(base)

            if i != n - 1:
                buy_hint = base[:]
                buy_hint[0] += hint[i][0]

                for k in hint[i][1:]:
                    buy_hint[k] += 1

                new_arr.append(buy_hint)

        arr = new_arr

    return min(a[0] for a in arr)