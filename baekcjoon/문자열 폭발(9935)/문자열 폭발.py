import sys
input = sys.stdin.readline

s = input().rstrip()
boom = list(input().rstrip())
n = len(boom)
stack = list(s[:n-1])

for i in range(n-1, len(s)):
    stack.append(s[i])
    if stack[-1] == boom[-1] and stack[-n:] == boom:
        for _ in range(n):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')
