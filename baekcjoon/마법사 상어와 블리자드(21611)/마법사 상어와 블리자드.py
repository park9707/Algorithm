import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n = N ** 2
board = [list(map(int, input().split())) for _ in range(N)]
arr = [0] * n  # 1차원 리스트로 생성
arr_dic = {}
move = ((-1, 0), (1, 0), (0, -1), (0, 1))
move_nums = {0: 2, 1: 3, 2: 1, 3: 0}  # 1차원 리스트로 만들기 위해 다음 이동할 방향 순서 지정
move_num = 2  # 처음은 왼쪽이므로 0, -1로 지정
x = y = (N + 1) // 2 - 1  # 상어의 위치
arr_idx = 1
ans = {1: 0, 2: 0, 3: 0}
# 1차원 리스트로 생성, 같은 횟수로 2번씩 도는 규칙이 있음
for i in range(1, N):
    for _ in range(2):
        dx, dy = move[move_num]
        tx, ty = x + (i * dx), y + (i * dy)
        while tx != x or ty != y:
            x += dx
            y += dy
            arr[arr_idx] = board[x][y]
            arr_dic[x, y] = arr_idx
            arr_idx += 1
        # 다음 이동할 방향
        move_num = move_nums[move_num]

# 2차원 좌표와 1차원 리스트 인덱스 값 매칭
for i in range(arr_idx, n):
    y -= 1
    arr[i] = board[x][y]
    arr_dic[x, y] = i

# 첫 위치 초기화
x = y = (N + 1) // 2 - 1
for i in range(M):
    d, s = map(int, input().split())
    dx, dy = move[d-1]
    nx, ny = x, y
    l = arr_dic[x + dx, y + dy]
    # s 거리 만큼 블리자드
    for _ in range(s):
        nx += dx
        ny += dy
        arr_idx = arr_dic[nx, ny]
        arr[arr_idx] = 0

    # 블리자드에서 pop()을 쓰는 것 보다 속도의 이점이 있으므로 반복문으로 0을 뒤쪽으로 빼기
    for r in range(l, n):
        if arr[r] != 0:
            arr[l], arr[r] = arr[r], 0
            l += 1

    is_explode = True
    while is_explode:
        is_explode = False
        l, r = 1, 2
        cnt = 1
        # arr[r]이 0이면 뒤쪽도 0이므로 더 할 필요가 없음
        while arr[r]:
            if arr[l] == arr[r]:
                cnt += 1
                r += 1
                continue
            # 구슬이 4개가 연속으로 있으면 터뜨리기
            elif cnt >= 4:
                ans[arr[l]] += cnt
                arr = arr[:l] + arr[r:] + ([0] * cnt)
                cnt = 1
                r = l + 1
                is_explode = True
            else:
                l = r
                r += 1
                cnt = 1

        if cnt >= 4:
            ans[arr[l]] += cnt
            arr = arr[:l] + arr[r:] + ([0] * cnt)
            is_explode = True

    new_arr = [0] * n
    cnt = 1
    l = 1

    for j in range(1, n, 2):
        for k in range(l, n-1):
            if arr[k] == arr[k+1]:
                cnt += 1
            else:
                new_arr[j] = cnt
                new_arr[j+1] = arr[k]
                cnt = 1
                l = k + 1
                break
        else:
            break
    arr = new_arr

print(ans[1] + (2 * ans[2]) + (3 * ans[3]))
