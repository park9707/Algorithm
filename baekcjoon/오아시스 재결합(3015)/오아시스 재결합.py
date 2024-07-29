import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = 0
for i in range(n):
    h = int(input())
    while stack and stack[-1][0] < h:
        ans += stack.pop()[1]

    if not stack:
        stack.append([h, 1])
    elif stack[-1][0] == h:
        cnt = stack.pop()[1]
        ans += cnt
        if stack:
            ans += 1

        stack.append([h, cnt + 1])
    else:
        stack.append([h, 1])
        ans += 1

print(ans)