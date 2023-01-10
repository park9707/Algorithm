def solution(n):
    answer = ''
    arr = {1:'1', 2:'2', 0:'4'}
    while n > 2:
        answer += arr[n%3]
        n //= 3
    answer += arr[n]
    return answer[::-1]