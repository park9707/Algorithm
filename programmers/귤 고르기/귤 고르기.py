def solution(k, tangerine):
    arr = {}
    
    for i in tangerine:
        if i in arr:
            arr[i] += 1
        else:
            arr[i] = 1

    arr_list = sorted(list(arr.values()), reverse = True)
    
    idx = 0
    
    while 0 < k:
        k -= arr_list[idx]
        idx += 1

    return idx
