def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n  # right 은 최악의 경우
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time  # mid 시간 동안 심사할 수 있는 사람 수

            if people >= n:  # 모두 심사 했다면 반복문 탈출
                break

        if people >= n:
            answer = mid
            right = mid - 1

        elif people < n:
            left = mid + 1

    return answer
