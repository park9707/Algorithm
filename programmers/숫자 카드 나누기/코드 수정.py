from math import gcd
from functools import reduce

def check(arrayA, arrayB):
    gcd_A = reduce(gcd, arrayA, arrayA[0])

    if all(i % gcd_A for i in arrayB):
        return gcd_A
    else:
        return 0

def solution(arrayA, arrayB):
    return max(check(arrayA, arrayB), check(arrayB, arrayA))
