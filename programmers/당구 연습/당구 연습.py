def solution(m, n, startX, startY, balls):
    answer = []

    def getDistance(x, y):
        return (x - startX) ** 2 + (y - startY) ** 2

    for bx, by in balls:
        min_distance = int(1e9)

        if not (startX == bx and startY > by):
            min_distance = min(min_distance, getDistance(bx, -by))

        if not (startX == bx and startY < by):
            min_distance = min(min_distance, getDistance(bx, 2 * n - by))

        if not (startY == by and startX > bx):
            min_distance = min(min_distance, getDistance(-bx, by))

        if not (startY == by and startX < bx):
            min_distance = min(min_distance, getDistance(2 * m - bx, by))

        answer.append(min_distance)

    return answer