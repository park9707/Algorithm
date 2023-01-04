def solution(word):
    answer = 0
    dic = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    value = [781, 156, 31, 6, 1]
    for idx, string in enumerate(word):
        answer += (dic[string]* value[idx]) + 1

    return answer