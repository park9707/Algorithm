from collections import deque

def bfs(start, visitied, graph):
    queue = deque([start]) # 시작 위치 담기
    result = 1 # 송전탑의 개수
    visitied[start] = True # 시작점 방문 처리
    while queue:
        now = queue.popleft() # 현재 위치

        for i in graph[now]: # 현재 위치에서 갈 수 있는 송전탑들
            if visitied[i] == False: # 송전탑을 방문하지 않았다면
                result += 1 # 송전탑 개수 +1
                queue.append(i) # 큐에 담는다.
                visitied[i] = True # 방문처리

    return result


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)] # 송전탑의 개수

    for v1, v2 in wires: # 와이어 반복해서 받아온다.
        graph[v1].append(v2) # 양쪽의 송전탑을 각각 담는다.
        graph[v2].append(v1)

    for start, not_visit in wires:
        visitied = [False] * (n + 1) # 방문 처리 리스트
        visitied[not_visit] = True # 방문 처리로 와이어 끊기
        result = bfs(start, visitied, graph) # 시작위치와 방문 처리 리스트, 그래프를 넘겨 bfs 실행
        if abs(result - (n - result)) < answer: # 절댓값을 씌워 결과값 차이가 answer보다 작으면 answer에 담는다.
            answer = abs(result - (n - result))

    return answer