def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        cnt = 1
        b = ''
        tmp = s[:i]
        
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    b += tmp
                else:
                    b += str(cnt) + tmp
                cnt = 1
                tmp = s[j:j+i]
        
        if cnt == 1:
            b += tmp
        else:
            b += str(cnt) + tmp
        
        answer = min(answer, len(b))
    
    return answer
