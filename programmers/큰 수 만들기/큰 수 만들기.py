def solution(number, k):
    i=0
    while k > 0 and i < len(number)-1:
        if number[i] >= number[i+1]:
            i+=1
            continue
        elif number[i] < number[i+1]:
            number = number[:i] + number[i+1:]
            k -= 1
            if i == 0:
                continue
            else:
                i -= 1
    if k > 0:
        number = number[:-k]
    return number

print(solution('4177252841', 4))