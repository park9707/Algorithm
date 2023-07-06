def solution(cards):
    n = len(cards)
    visited = [False] * n
    boxes = []
    arr = []
    for i in range(n):
        while not visited[i]:
            visited[i] = True
            i = cards[i] - 1
            arr.append(i)
        if arr:
            boxes.append(len(arr))
            arr = []
    boxes.sort()

    return boxes[-1] * boxes[-2] if len(boxes) > 1 else 0
