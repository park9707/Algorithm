from itertools import permutations
from collections import deque


def solution(expression):
    answer = 0
    arr = deque()
    op = set()
    num = ''
    for k in expression: # 입력 받은 문자열 돌기
        if k.isdigit(): # 문자가 숫자면
            num += k # num에 합치기
        else: # 숫자가 아니라면
            arr.append(num) # 리스트에 합친 숫자 삽입
            num = '' # 변수 초기화
            arr.append(k) # 리스트에 연산자 삽입
            op.add(k) # 입력 받은 연산자만 순열로 만들기 위해 삽입
    arr.append(num) # 마지막 숫자 삽입

    a = list(permutations(op, len(op))) # 연산자들로 만들 수 있는 경우의 수 담기

    for j in a: # 순열 하나씩 넘기기
        lst = arr.copy()
        for op in j:
            stack = []
            while len(lst) > 0: # 리스트가 빌 때까지
                tmp = lst.popleft()
                if tmp == op: # 우선순위 연산자라면
                    result = str(eval(stack.pop() + op + lst.popleft())) # 스택에 있는 값과 리스트에 있는 값 연산 결과
                    stack.append(result) # 연산 결과값 스택에 추가
                else:
                    stack.append(tmp) # 스택에 문자 삽입
            lst = deque(stack)
        answer = max(answer, abs(int(lst.pop())))
    return answer