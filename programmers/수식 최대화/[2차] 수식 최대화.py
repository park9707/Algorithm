from itertools import permutations


def cal(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b


def solution(expression):
    answer = 0
    op_set = set()
    ex = []
    num = ''
    for i in expression:
        if i.isdigit():
            num += i
        else:
            ex.append(num)
            ex.append(i)
            op_set.add(i)
            num = ''
    ex.append(num)

    for ops in permutations(op_set):
        result = ex.copy()
        for op in ops:
            stack = [result[0]]
            for i in range(1, len(result), 2):
                if result[i] == op:
                    stack.append(cal(int(stack.pop()), int(result[i + 1]), op))
                else:
                    stack.append(result[i])
                    stack.append(result[i + 1])
            result = stack
        answer = max(answer, abs(stack[0]))

    return answer
