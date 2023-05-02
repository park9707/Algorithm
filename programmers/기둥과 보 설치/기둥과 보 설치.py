def c_possible(x, y, frame):
    global graph
    # 기둥 설치 시 확인 해야 할 것 : 밑 기둥, 왼쪽 보, 같은 자리 보
    if frame == 0:  # 기둥일 때
        if y == 0:  # 바닥이면 설치 가능
            return True
        if 0 in graph[y - 1][x]:  # 밑에 기둥이 있다면 설치 가능
            return True
        if 1 in graph[y][x - 1] or 1 in graph[y][x]:  # 왼쪽이나 같은 자리에 보가 있다면 설치 가능
            return True
        return False  # 그 외의 경우 설치 불가
    # 보 설치 시 확인 해야 할 것 : 아래 기둥, 오른쪽 아래 기둥, 왼쪽과 오른쪽 보
    elif frame == 1:  # 보 일때
        if 0 in graph[y - 1][x] or 0 in graph[y - 1][x + 1]:  # 아래에 기둥이 있거나 오른쪽 아래에 기둥이 있다면 설치 가능
            return True
        if 1 in graph[y][x - 1] and 1 in graph[y][x + 1]:  # 왼쪽과 오른쪽에 보가 있다면 설치 가능
            return True
        return False  # 그 외의 경우 설치 불가


def d_possible(x, y, frame):
    global graph
    # 기둥 삭제 시 확인 해야 할 것 : 위 기둥, 위 보, 왼쪽 위 보
    if frame == 0:  # 기둥일 때
        if 0 in graph[y + 1][x]:  # 위에 기둥이 있다면
            if 1 not in graph[y + 1][x] and 1 not in graph[y + 1][x - 1]:  # 위 기둥을 지탱하는(왼쪽과 그 자리) 보가 없다면 삭제 불가
                return False
        if 1 in graph[y + 1][x]:  # 위에 보가 있다면
            # 위의 보를 지탱할 오른쪽에 기둥이나 양쪽의 보 중 하나라도 없다면 삭제 불가
            if 0 not in graph[y][x + 1] and (1 not in graph[y + 1][x - 1] or 1 not in graph[y + 1][x + 1]):
                return False
        if 1 in graph[y + 1][x - 1]:  # 왼쪽 위 보가 있다면
            # 왼쪽 위 보를 지탱할 왼쪽 아래 기둥이나 양쪽 보가 없으면 삭제 불가
            if 0 not in graph[y][x - 1] and (1 not in graph[y + 1][x - 2] or 1 not in graph[y + 1][x]):
                return False
        return True
    # 보 삭제 시 확인 해야 할 것 : 같은 자리 기둥, 오른쪽 기둥, 왼쪽 보, 오른쪽 보
    elif frame == 1:
        if 0 in graph[y][x]:  # 같은 자리 기둥이 있다면
            # 기둥을 지탱할 아래쪽 기둥이나 왼쪽 보가 없다면 삭제 불가
            if 0 not in graph[y - 1][x] and 1 not in graph[y][x - 1]:
                return False
        if 0 in graph[y][x + 1]:  # 오른쪽 기둥이 있다면
            # 오른쪽 기둥을 지탱할 그 아래 기둥이나 오른쪽 보가 없다면 삭제 불가
            if 0 not in graph[y - 1][x + 1] and 1 not in graph[y][x + 1]:
                return False
        if 1 in graph[y][x - 1]:  # 왼쪽 보가 있다면
            # 왼쪽 보를 지탱할 그 아래 기둥이나 아래쪽 기둥이 없다면 삭제 불가
            if 0 not in graph[y - 1][x - 1] and 0 not in graph[y - 1][x]:
                return False
        if 1 in graph[y][x + 1]:  # 오른쪽 보가 있다면
            # 오른쪽 보를 지탱할 그 아래 기둥이나 그 오른쪽 아래 기둥이 없다면 삭제 불가
            if 0 not in graph[y - 1][x + 1] and 0 not in graph[y - 1][x + 2]:
                return False
        return True


def solution(n, build_frame):
    global graph
    graph = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    for x, y, frame, cd in build_frame:
        if cd == 1:
            if c_possible(x, y, frame):
                graph[y][x].append(frame)
        elif cd == 0:
            if d_possible(x, y, frame):
                graph[y][x].remove(frame)

    result = []
    for i in range(n+1):
        for j in range(n+1):
            for k in sorted(graph[j][i]):  # 값이 있는 곳만 x, y, 기둥과 보 순으로 정렬
                result.append([i, j, k])
    return result
