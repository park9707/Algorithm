def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1
    for i in range(begin, end + 1):
        num = 1
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                if i // j > 10000000:
                    num = j
                    continue
                else:
                    num = i // j
                    break
        answer.append(num)

    return answer
