import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
answer = [-1] * n
stack = []

for i in range(n-1, -1, -1):
    while stack:
        temp = stack.pop()
        if a[i] < temp:
            answer[i] = temp
            stack.append(temp)
            break
    stack.append(a[i])

print(' '.join(map(str, answer)))
