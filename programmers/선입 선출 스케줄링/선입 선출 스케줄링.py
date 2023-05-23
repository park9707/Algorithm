def solution(n, cores):
    n -= len(cores)
    left, right = 1, max(cores) * n
    while left < right:
        mid = (right + left) // 2
        temp = 0
        for core in cores:
            temp += mid // core

        if temp >= n:
            right = mid
        else:
            left = mid + 1

    for core in cores:
        n -= (right - 1) // core

    for i in range(len(cores)):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1