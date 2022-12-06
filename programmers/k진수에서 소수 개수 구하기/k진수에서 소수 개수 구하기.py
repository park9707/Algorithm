import math

def solution(n, k):
    k_num = to_k_number(n, k)
    answer = 0
    for i in k_num.split('0'):
        if i == '': continue
        if is_prime_number(int(i)):
            answer += 1
    return answer
         
def to_k_number(n, k):
    ret = ''
    while n > 0:
        ret += str(n % k)
        n = n // k
    return ret[::-1]

def is_prime_number(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True
