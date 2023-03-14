def solution(cap, n, deliveries, pickups):
    answer = 0
    d = p = 0
    for i in range(n - 1, -1, -1):  # 가장 먼 곳 부터
        d += deliveries[i]  # i 번째의 배달 량
        p += pickups[i]  # i 번째의 수거 량

        while d > 0 or p > 0:  # 배달 또는 수거 해야 할 것이 있다면 무조건 와야함
            d -= cap  # 최대 적재량 만큼 빼기
            p -= cap  # 최대 적재량 만큼 빼기
            answer += (i+1) * 2  # 왕복을 해야 하므로 가장 먼 거리 * 2
        # 첫 배달 또는 수거 이후 양수가 되어야 와야 될 지역, 음수라면 가장 먼 곳을 가는 김에 배달 또는 수거 가능
    return answer
