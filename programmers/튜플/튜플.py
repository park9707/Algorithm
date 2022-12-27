def solution(s):
    answer = []
    s=s[2:-2].split('},{')
    a = {}
    for i in s:
        for k in i.split(','):
            if k in a:
                a[k] += 1
            else:
                a[k] = 1

    b = sorted(a.items(), key = lambda x : x[1], reverse = True)

    for i in b:
        answer.append(int(i[0]))

    return answer