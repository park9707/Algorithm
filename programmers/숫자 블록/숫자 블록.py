def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1
    for i in range(begin, end+1):
        a = 1
        for j in range(2, int(i**0.5)+1):
            if i % j == 0 and i//j <= 10000000:
                a = i//j
                break
        answer.append(a)
    return answer

# 문제 수정 후 틀린 코드가 됐다.
