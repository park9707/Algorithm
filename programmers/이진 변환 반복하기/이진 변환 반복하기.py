def solution(s):
    cnt = cnt_zero = 0
    
    while len(s) > 1:
        cnt_zero += s.count('0')
        s = ''.join(s.split('0'))
        cnt += 1
        s = format(len(s),'b')
        
    return [cnt, cnt_zero]
