def solution(n, s, a, b, fares):
    d = [[float('inf') for _ in range(n)] for _ in range(n)]  # 맥스 값으로 행렬 생성

    for x in range(n):  # 자기 자신은 비용 0
        d[x][x] = 0
    for x, y, c in fares:  # 경로와 비용
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):  # 거쳐가는 곳
        for j in range(n):  # 시작점
            for k in range(n):  # 도착점
                if d[j][k] > d[j][i] + d[i][k]:  # 현재 비용보다 i를 거쳐가는 것이 비용이 더 작으면
                    d[j][k] = d[j][i] + d[i][k]  # 변경

    answer = float('inf')

    for i in range(n):
        answer = min(answer, d[s-1][i]+d[i][a-1]+d[i][b-1])  # 출발점에서 i를 거쳐 가는 것과 answer 비교

    return answer
