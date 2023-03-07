def solution(book_time):
    t = []
    for s, e in book_time:
        s = int(s[:2]) * 60 + int(s[3:])
        e = int(e[:2]) * 60 + int(e[3:])
        t.append([s, 1])
        t.append([e + 10, 2])

    t.sort(key=lambda x: (x[0], -x[1]))

    room = 0
    answer = 0

    for i in t:
        if i[1] == 1:
            room += 1
        if i[1] == 2:
            room -= 1
        answer = max(answer, room)

    return answer
