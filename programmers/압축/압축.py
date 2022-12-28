def solution(msg):
    answer = []
    dic = {}
    value = 1
    dict_value = 27
    for i in range(65, 91):
        dic[chr(i)] = value
        value += 1

    start = 0
    end = 1
    while end <= len(msg)+1:
        if end == len(msg)+1:
            answer.append(dic[msg[start:end]])
            break
        elif msg[start:end] in dic.keys():
            end += 1
        else:
            dic[msg[start:end]] = dict_value
            answer.append(dic[msg[start:end-1]])
            dict_value += 1
            start = end-1
            end = start+1

    return answer