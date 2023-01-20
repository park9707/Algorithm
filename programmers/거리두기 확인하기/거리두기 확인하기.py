from collections import deque

def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i)) # 대기실 하나씩 bfs

    return answer

def bfs(room):
    start = []

    for i in range(5):  # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if room[i][j] == 'P':
                start.append([i, j])

    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0] * 5 for i in range(5)]  # 방문 처리 리스트
        distance = [[0] * 5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1  # 시작 지점은 방문처리

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:  # 벽이 아니고 방문하지 않았다면

                    if room[ny][nx] == 'O':  # 이동한 곳이 테이블이면
                        visited[ny][nx] = 1  # 방문처리
                        if distance[y][x] < 1: # 시작점의 거리가 1이라면 큐에 더 담지 않아도 된다.
                            queue.append([ny, nx])  # 큐에 추가
                            distance[ny][nx] = distance[y][x] + 1

                    if room[ny][nx] == 'P':  # 이동한 곳이 P라면
                        return 0

    return 1