def solution(numbers):
    answer = []
    for i in numbers:
        b = i+1
        if b&i == 0:
            a = b|(i>>1)
            answer.append(a)
        else:
            a = i|b
            a -= (a-i)//2
            answer.append(a)
    return answer