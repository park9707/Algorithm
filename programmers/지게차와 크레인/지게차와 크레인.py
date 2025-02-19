def fork(storage, visited, arr, s):
    new_stack = []
    cnt = 0
    move = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for x, y in arr:
        if storage[x][y] == s:
            cnt += 1
            visited[x][y] = 2
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == 0:
                        new_stack.append([nx, ny])
                        visited[nx][ny] = 1
                    elif visited[nx][ny] == 3:
                        check = [[nx, ny]]
                        visited[nx][ny] = 2
                        while check:
                            tx, ty = check.pop()
                            for tdx, tdy in move:
                                tnx = tx + tdx
                                tny = ty + tdy
                                if 0 <= tnx < n and 0 <= tny < m:
                                    if visited[tnx][tny] == 1 or visited[tnx][tny] == 2:
                                        continue
                                    elif visited[tnx][tny] == 0:
                                        new_stack.append([tnx, tny])
                                        visited[tnx][tny] = 1
                                    elif visited[tnx][tny] == 3:
                                        check.append([tnx, tny])
                                        visited[tnx][tny] = 2

        else:
            new_stack.append([x, y])
    return new_stack, cnt


def crane(storage, visited, s):
    cnt = 0
    for x in range(n):
        for y in range(m):
            if storage[x][y] == s and visited[x][y] == 0:
                cnt += 1
                visited[x][y] = 3
    return cnt


def solution(storage, requests):
    global n, m
    n, m = len(storage), len(storage[0])
    # 지게차가 접근 가능한 컨테이너
    container = []
    # 0 = 지게차가 접근 못함, 1 = 지게차가 접근 가능, 2 = 컨테이너가 꺼내진 곳, 3 = 크레인이 꺼낸 곳
    visited = [[0] * m for _ in range(n)]
    ans = n * m

    for i in range(m):
        container.append([0, i])
        container.append([n - 1, i])
        visited[0][i] = 1
        visited[n - 1][i] = 1

    for i in range(1, n-1):
        container.append([i, 0])
        container.append([i, m - 1])
        visited[i][0] = 1
        visited[i][m - 1] = 1

    for req in requests:
        if len(req) != 1:
            ans -= crane(storage, visited, req[0])
        new_container, cnt = fork(storage, visited, container, req[0])
        ans -= cnt
        container = new_container
    return ans
