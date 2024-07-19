import sys
input = sys.stdin.readline

while True:
    graph = list(map(int, input().split()))

    if graph[0] == 0:
        break

    stack = []
    ans = 0

    for i in range(1, graph[0] + 1):
        h = graph[i]

        while stack and stack[-1][1] > h:
            _, stack_h = stack.pop()
            w = i - (stack[-1][0] + 1) if stack else i - 1
            cal_result = w * stack_h
            ans = max(ans, cal_result)

        stack.append([i, h])

    i = graph[0] + 1
    while stack:
        _, stack_h = stack.pop()
        w = i - (stack[-1][0] + 1) if stack else i - 1
        cal_result = w * stack_h
        ans = max(ans, cal_result)

    print(ans)
