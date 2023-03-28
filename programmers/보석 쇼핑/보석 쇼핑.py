from collections import Counter

def solution(gems):
    n = len(set(gems))  # 보석의 종류
    answer = [1, len(gems)]
    l = 0  # 왼쪽 인덱스 값
    r = n
    dic = Counter(gems[:r])

    while r < len(gems):
        while len(dic) < n and r < len(gems):
            dic[gems[r]] += 1  # gems[r] 보석의 개수 + 1
            r += 1

        while len(dic) == n:  # 보석을 최소 한개씩 샀다면
            dic[gems[l]] -= 1  # 딕셔너리에서 왼쪽 인덱스의 보석 하나 빼보기
            if dic[gems[l]] == 0:  # 빼서 0이 됐다면
                del dic[gems[l]]  # 딕셔너리에서 없애기
            l += 1
            if r-l < answer[1] - answer[0]:  # 차이가 더 작다면 l과 r값을 넣고 아니라면 먼저 입력했던 answer 값
                answer = [l, r]

    return answer
