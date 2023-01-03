def solution(elements):
    answer = set()
    length = len(elements)
    elements = elements * 2
    for i in range(length):
        for j in range(i+1, length+i+1):
            answer.add(sum(elements[i:j]))
    return len(answer)