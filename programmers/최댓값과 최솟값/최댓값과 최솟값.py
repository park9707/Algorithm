def solution(s):
    arr = list(map(int, s.split()))
    arr.sort()
    answer = str(arr[0]) + ' ' + str(arr[len(arr)-1])
    return answer
