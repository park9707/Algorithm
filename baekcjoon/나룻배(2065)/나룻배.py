import sys, collections
input = sys.stdin.readline

M, t, N = map(int, input().split())
left_q = collections.deque()
right_q = collections.deque()
is_right = False
current_t = 0
m = M
ans = [0] * N

for i in range(N):
    a, b = input().split()
    if b == 'left':
        left_q.append([int(a), i])
    else:
        right_q.append([int(a), i])

left_q.append([float('inf')])
right_q.append([float('inf')])

while left_q[0][0] != float('inf') or right_q[0][0] != float('inf'):
    # 현재 배가 왼쪽일 경우
    if not is_right:
        while left_q[0][0] <= current_t and m > 0:
            m -= 1
            _, b = left_q.popleft()
            ans[b] = current_t + t
    # 현재 배가 오른쪽일 경우
    elif is_right:
        while right_q[0][0] <= current_t and m > 0:
            m -= 1
            _, b = right_q.popleft()
            ans[b] = current_t + t

    # 태운 손님이 없을 경우
    if m == M:
        # 왼쪽 손님이 먼저 도착할 경우
        if left_q[0][0] < right_q[0][0]:
            if not is_right:
                current_t = left_q[0][0]
            else:
                is_right = not is_right
                current_t = max(current_t, left_q[0][0]) + t
        # 오른쪽 손님이 먼저 도착할 경우
        elif left_q[0][0] > right_q[0][0]:
            if is_right:
                current_t = right_q[0][0]
            else:
                is_right = not is_right
                current_t = max(current_t, right_q[0][0]) + t
        # 양쪽 손님 동시에 도착할 경우
        else:
            current_t = right_q[0][0]
    # 손님을 태웠다면 이동
    else:
        m = M
        is_right = not is_right
        current_t += t

for i in range(N):
    print(ans[i])