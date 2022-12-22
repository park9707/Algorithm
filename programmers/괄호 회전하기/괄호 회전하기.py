def check(s):
    stack = []
    for i in s: #s의 괄호를 하나씩 받아와서
        if len(stack) == 0: #스택이 비어있다면 바로 삽입
            stack.append(i)
        else:
            if i == ")" and stack[-1] == "(": #먼저 삽입한 것과 올바른 조합이라면
                stack.pop() #스택에서 제거
            elif i == "]" and stack[-1] == "[": #반복
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i) #삽입한 것들과 올바른 조합이 아니라면 스택에 삽입
    return not stack #모두 올바른 조합이면 1 리턴

def solution(s):
    answer = 0

    for i in range(len(s)):
        if check(s):
            answer += 1
        s = s[1:] + s[0] #괄호 회전

    return answer