from collections import defaultdict


def solution(tickets):
    route = defaultdict(list)
    for a, b in tickets:
        route[a].append(b)
    for key in route:
        route[key].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while stack:
        temp = stack[-1]
        if temp not in route or not route[temp]:
            path.append(stack.pop())
        else:
            stack.append(route[temp].pop())
    return path[::-1]
