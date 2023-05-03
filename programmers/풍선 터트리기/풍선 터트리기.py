def solution(a):
    answer = 0
    left_min = right_min = float('inf')

    for i in range(len(a)):
        if a[i] < left_min:
            answer += 1
            left_min = a[i]
        if a[-1 - i] < right_min:
            answer += 1
            right_min = a[-1 - i]

    return answer - 1  # 전체 중 최솟값은 무조건 answer을 2번 올리기 때문에 -1