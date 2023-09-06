import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(num):
    next_num = target[num]
    # 다음 번호가 자기 자신이라면 자신은 팀o 반환값 0
    if next_num == num:
        visited[num] = 2
        return 0
    # 다음 번호를 방문하지 않았다면
    elif not visited[next_num]:
        # 현재 번호 방문처리, 체크 중
        visited[num] = 1
        j = dfs(next_num)
        # 리턴 값이 0이 아닌 경우
        if j != 0:
            visited[num] = 2
            if num == j:
                return 0
            return j
        # 리턴 값이 0이면 팀 x
        else:
            visited[num] = 3
            return 0
    else:
        # 다음 번호 방문했고, 체크 중인 상태라면 팀o
        if visited[next_num] == 1:
            visited[num] = 2
            return next_num
        else:
            visited[num] = 3
            return 0


t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    target = [0] + list(map(int, input().rstrip().split()))
    # 0: 방문x, 1: 방문o 체크 중, 2: 방문o 팀o, 3: 방문o 팀x
    visited = [0] * (n + 1)
    team = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = 1
            if target[i] == i:
                visited[i] = 2
            else:
                j = dfs(i)

    print(visited.count(3))
