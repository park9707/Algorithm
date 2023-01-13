from collections import deque


def time_(split_info):
    s_time = list(map(int, split_info[0].split(':')))
    e_time = list(map(int, split_info[1].split(':')))
    s_min = s_time[0] * 60 + s_time[1]
    e_min = e_time[0] * 60 + e_time[1]
    return e_min - s_min


def solution(m, musicinfos):
    answer = '(None)'
    max_t = 0
    for i in musicinfos:
        split_info = i.split(',')
        t = time_(split_info)
        if t <= max_t:
            continue

        q = deque()
        s = ''
        for j in split_info[3]:
            if j.isalpha() and s:
                q.append(s)
                s = j
            else:
                s += j
        q.append(s)

        if len(q) < t + 1:
            for i in range(t + 1 - len(q)):
                q.append(q[i])

        elif len(q) > t + 1:
            q = deque(list(q)[:t + 1])

        n = 0
        while n < len(q):
            join_str = ''.join(q)
            split_str = join_str.split(m)
            if m in join_str:
                if split_str[1] == '' or split_str[1][0].isalpha():
                    answer = split_info[2]
                    max_t = t
                    break
                else:
                    q.append(q.popleft())
                    n += 1
            else:
                q.append(q.popleft())
                n += 1
    return answer