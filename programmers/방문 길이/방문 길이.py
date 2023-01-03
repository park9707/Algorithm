def solution(dirs):
    x, y = 0, 0
    visit = set()
    for i in dirs:
        if i == 'U' and y < 5:
            visit.add(((x, y), (x, y + 1)))
            y += 1
        elif i == 'D' and y > -5:
            visit.add(((x, y - 1), (x, y)))
            y -= 1
        elif i == 'R' and x < 5:
            visit.add(((x, y), (x + 1, y)))
            x += 1
        elif i == 'L' and x > -5:
            visit.add(((x - 1, y), (x, y)))
            x -= 1

    return len(visit)