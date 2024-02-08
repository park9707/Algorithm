def change_range(pre_t1, pre_t2, pre_temperature, num):
    return [pre_t1 + num, pre_t2 + num, pre_temperature + num]


def solution(temperature, t1, t2, a, b, onboard):
    if t1 < 0:
        t1, t2, temperature = change_range(t1, t2, temperature, t1)
    elif temperature < 0:
        t1, t2, temperature = change_range(t1, t2, temperature, temperature)

    if t1 < temperature:
        t1, t2, temperature = change_range(t1, t2, temperature, -t1 + 1)
        off = -1
    else:
        t1, t2, temperature = change_range(t1, t2, temperature, -temperature + 1)
        off = 1
    on = -off
    max_y = max(t2, temperature)
    n = len(onboard)
    dp = [[100 * 50 * 1000] * (max_y + 2) for _ in range(n)]
    dp[0][temperature] = 0

    for i in range(1, n):
        left, right = [t1, t2] if onboard[i] else [1, max_y]
        for j in range(left, right+1):
            if j == temperature:
                dp[i][j] = min(dp[i-1][j+on] + a, dp[i-1][j+off], dp[i-1][j])
                continue
            dp[i][j] = min(dp[i-1][j+on] + a, dp[i-1][j+off], dp[i-1][j] + b)

    return min(dp[-1])
