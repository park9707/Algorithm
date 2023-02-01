def solution(storey):
    answer = 0
    while storey:
        a = storey % 10
        if a > 5:
            answer += (10 - a)
            storey += 10
        elif a < 5:
            answer += a
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += a
        storey //= 10

    return answer