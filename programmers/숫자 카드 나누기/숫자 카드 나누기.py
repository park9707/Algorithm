import math
def solution(arrayA, arrayB):
    answer = [0]

    gcd_a = arrayA[0]
    gcd_b = arrayB[0]

    for i, j in zip(arrayA[1:], arrayB[1:]):
        gcd_a, gcd_b = math.gcd(gcd_a, i), math.gcd(gcd_b, j) 

    for i in arrayB:
        if i % gcd_a == 0:
            break
    else:
        answer.append(gcd_a)

    for j in arrayA:
        if j % gcd_b == 0:
            break
    else:
        answer.append(gcd_b)
        
    return max(answer)
