def solution(n, m, x, y, r, c, k):
    answer = []
    dist = abs(x - r) + abs(y - c)  # 출발 지점부터 도착 지점까지 거리
    k -= dist  # 이동 가능 거리에서 dist 빼기
    if k < 0 or k % 2 != 0:  # 도착 지점에서 남은 k가 짝수가 아니거나 k가 음수면 이동 불가
        return "impossible"

    direction = {'d': 0, 'l': 0, 'r': 0, 'u': 0}  # 도착 지점까지 각 방향으로 이동 해야할 거리
    if x > r:
        direction['u'] += x - r
    else:
        direction['d'] += r - x
    if y > c:
        direction['l'] += y - c
    else:
        direction['r'] += c - y

    answer += ['d'] * direction['d']  # 아래로 가야한다면 그 만큼 이동
    d = min(k // 2, n - (x + direction['d']))  # 이동 가능 거리 k의 반(왕복 고려)와 미로의 아래쪽 끝 중 더 짧은 것 담음
    answer += ['d'] * d  # 정답에 'd'를 위의 d 변수만큼 추가
    direction['u'] += d  # 내려온 만큼 올라 가야 함
    k -= 2 * d  # 왕복만큼 빼기

    answer += ['l'] * direction['l']  # 왼쪽으로 가야한다면 그 만큼 이동
    l = min(k // 2, y - direction['l'] - 1)  # 이동 가능 거리 k의 반(왕복 고려)와 미로의 왼쪽 끝 중 더 짧은 것 담음
    answer += ['l'] * l  # 정답에 'l'을 위의 l 변수만큼 추가
    direction['r'] += l  # 왼쪽으로 이동한 만큼 오른쪽으로 이동해야 함
    k -= 2 * l  # 왕복만큼 빼기

    answer += ['r', 'l'] * (k // 2)  # 왼쪽 아래에서 반복 가능한 가장 사전순으로 빠른 것 남은 이동 수 만큼 반복
    answer += ['r'] * direction['r']  # 오른쪽으로 이동해야 할 만큼 이동
    answer += ['u'] * direction['u']  # 위쪽으로 이동해야 할 만큼 이동
    return ''.join(answer)  # 리스트에 담은 것 한 문자로 합치기

print(solution(	3, 4, 2, 3, 3, 1, 5))