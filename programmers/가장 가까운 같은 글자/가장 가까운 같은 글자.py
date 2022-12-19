def solution(s):
    answer = [-1]
    for i in range(1, len(s)):
        idx = -1
        if s[i] in s[:i]:
            for j in range(0, i):
                if s[i] == s[j]:
                    idx = i - j
                
        answer.append(idx)
            
    return answer
