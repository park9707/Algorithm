def solution(storey):
    answer = 0

    while storey:
        num = storey % 10
        if num > 5:
            answer += (10 - num)
            storey += 10
        elif num == 5 and storey // 10 % 10 > 4:
            storey += 10
            answer += (10 - num)
        else:
            answer += num
        storey //= 10

    return answer
