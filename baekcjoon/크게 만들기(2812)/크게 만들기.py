import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = input().rstrip()
stack = [num[0]]

for i in range(1, n):
    while stack and stack[-1] < num[i] and 0 < k:
        stack.pop()
        k -= 1
    stack.append(num[i])

if k == 0:
    print(''.join(stack))
else:
    print(''.join(stack[:-k]))
