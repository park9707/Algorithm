def solution(diffs, times, limit):
    max_level, min_level = max(diffs), 1

    while min_level < max_level:
        mid = (min_level + max_level) // 2
        n = times[0]
        for i in range(1, len(diffs)):
            n += max(diffs[i] - mid, 0) * (times[i - 1] + times[i]) + times[i]

        if n > limit:
            min_level = mid + 1
        else:
            max_level = mid
    return min_level
