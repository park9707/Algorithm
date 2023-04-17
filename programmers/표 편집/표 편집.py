def solution(n, k, cmd):
    linked_list = {i: [i-1, i+1] for i in range(n)}
    answer = ['O'] * n
    stack = []

    for cmd in cmd:
        if cmd == 'C':
            prev, nxt = linked_list[k]
            answer[k] = 'X'
            stack.append([k, prev, nxt])

            if nxt == n:
                k = linked_list[k][0]
                linked_list[k][1] = nxt
                linked_list[prev][1] = nxt
            else:
                k = linked_list[k][1]
                linked_list[k][0] = prev

            if prev == -1:
                linked_list[nxt][0] = prev
            elif nxt == n:
                linked_list[prev][1] = nxt
            else:
                linked_list[nxt][0] = prev
                linked_list[prev][1] = nxt

        elif cmd == 'Z':
            tmp, prev, nxt = stack.pop()
            answer[tmp] = 'O'
            if prev == -1:
                linked_list[nxt][0] = tmp
            elif nxt == n:
                linked_list[prev][1] = tmp
            else:
                linked_list[nxt][0] = tmp
                linked_list[prev][1] = tmp

        else:
            direction, num = cmd.split()
            num = int(num)
            if direction == 'U':
                for _ in range(num):
                    k = linked_list[k][0]
            elif direction == 'D':
                for _ in range(num):
                    k = linked_list[k][1]

    return ''.join([i for i in answer])
