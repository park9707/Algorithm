from math import factorial

def solution(n, k):
    answer = [i for i in range(1, n + 1)]
    stack = []
    k -= 1

    while answer:
        n -= 1
        a = k // factorial(n)
        stack.append(answer[a])
        del answer[a]

        k = k % factorial(n)

    return stack