def solution(s):
    arr = [s[0]]
    for i in range(1, len(s)):
        if s[i] == ''.join(arr[len(arr)-1 : len(arr)]):
            arr.pop()
        else:
            arr.append(s[i])

    if not arr:
        return 1
    else:
        return 0