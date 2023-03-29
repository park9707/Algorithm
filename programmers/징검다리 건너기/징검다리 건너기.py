def solution(stones, k):
    left = 1
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2  # 중간 값
        cnt = 0  # 못건너는 돌 카운트
        for stone in stones:
            if stone - mid < 0:  # 중간 값 뺐을 때 못건너는 사람이 있다면
                cnt += 1  # 카운트 +1
                if cnt >= k:  # 연속으로 못건너는 돌이 k개 이상이면
                    right = mid - 1  # 건널 사람 줄이기
                    break
            else:
                cnt = 0  # 아니면 초기화
        else:  # break로 탈출하지 않았다면 mid명 건널 수 있다.
            left = mid + 1  # 건널 사람 늘리기

    return left-1

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
