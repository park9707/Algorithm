import sys, collections
input = sys.stdin.readline

n = int(input().rstrip())
# 0: 자기 자신이 있어서 이동 불가, 1: 이동 가능, 2: 사과
board = [[1] * n for _ in range(n)]
k = int(input().rstrip())
# 사과 좌표 위치 2로 바꾸기
for _ in range(k):
    x, y = map(int, input().rstrip().split())
    board[x-1][y-1] = 2
l = int(input().rstrip())
# 회전해야 할 시간 및 방향, 마지막 전진을 위해 [0, 0] 추가
rotation = [list(input().rstrip().split()) for _ in range(l)] + [['0', '0']]
move = ((0, 1), (1, 0), (0, -1), (-1, 0))
# 회전
move_rotation = {0: (3, 1), 1: (0, 2), 2: (1, 3), 3: (2, 0)}

# 뱀이 차지하고 있는 좌표
q = collections.deque([[0, 0]])
# x, y: 머리의 위치, direction: 가고 있는 방향, cnt: 이동한 시간, i: 회전해야 할 시간 및 방향의 인덱스
x, y, direction, cnt, i = 0, 0, 0, 0, 0

for target_t, target_d in rotation:
    dx, dy = move[direction]
    target_t = int(target_t)
    temp = direction
    # 방향 바꾸기 전까지 계속 전진
    while temp == direction:
        x = x + dx
        y = y + dy
        cnt += 1
        if 0 <= x < n and 0 <= y < n and 0 < board[x][y]:
            q.append([x, y])
            # 다음 칸에 사과가 아니라면
            if board[x][y] == 1:
                tail_x, tail_y = q.popleft()
                # 꼬리였던 부분 이동 가능
                board[tail_x][tail_y] = 1
            board[x][y] = 0

            # 방향 바꿔야 하는 시간
            if target_t == cnt:
                if target_d == 'L':
                    direction = move_rotation[direction][0]
                else:
                    direction = move_rotation[direction][1]
        # 다음 칸을 이동할 수 없다면 break
        else:
            break
    # 방향이 바뀌었다면 continue로 계속 진행
    else:
        continue
    # 이동하지 못해 break로 나왔다면 반복문을 끝낸다.
    break

print(cnt)