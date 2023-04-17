def solution(prices):
    n = len(prices)-1
    stack = []
    answer = [0] * (n+1)

    for i, v in enumerate(prices):
        while stack and stack[-1][1] > v:
            idx, num = stack.pop()
            answer[idx] = i - idx
        stack.append([i, v])
    for i, v in stack:
        answer[i] = n - i

    return answer
