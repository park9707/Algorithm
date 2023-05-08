def time_to_sec(time):
    h, m, s = map(int, time.split(':'))
    return (h * 3600) + (m * 60) + s


def time_to_hour(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time %= 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    s = time % 60
    s = '0' + str(s) if s < 10 else str(s)
    return h + ':' + m + ':' + s


def solution(play_time, adv_time, logs):
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    all_time = [0] * (play_time + 1)
    n = len(all_time)

    for log in logs:
        start_time, end_time = log.split('-')
        start_time = time_to_sec(start_time)
        end_time = time_to_sec(end_time)
        all_time[start_time] += 1
        all_time[end_time] -= 1

    for i in range(1, n):
        all_time[i] += all_time[i - 1]

    for i in range(1, n):
        all_time[i] += all_time[i - 1]

    answer = 0
    most_view = all_time[adv_time]
    for i in range(adv_time + 1, n):
        if most_view < all_time[i] - all_time[i - adv_time]:
            most_view = all_time[i] - all_time[i - adv_time]
            answer = i - (adv_time - 1)

    return time_to_hour(answer)
