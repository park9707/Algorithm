from heapq import heappush, heappop

def solution(k, n, reqs):
    max_n = n - k
    map_k_reqs = {}
    wait_init = 0
    wait_diff = []

    for k_ in range(k):
        map_k_reqs[k_] = []

    for r in reqs:
        map_k_reqs[r[2] - 1].append(r[:2])

    # 상담 유형 하나 씩 진행
    for k_ in range(k):
        wait_k_ = 0

        # 상담원이 한명씩 늘어날 때 마다 줄일 수 있는 시간을 계산
        for n_ in range(max_n + 1):
            heap_n = []
            wait_time = 0

            # 상담원들을 heapq에 넣어 둠
            for _ in range(n_ + 1):
                heappush(heap_n, 0)

            # 상담 수 만큼 반복
            for req in map_k_reqs[k_]:
                # 제일 빨리 끝나는 상담원 한명을 꺼냄, 초기엔 0
                min_time = heappop(heap_n)

                # 요청의 시작 시간보다 작으면 = 상담을 안하고 있는 상담원이 있다면, 이 상담원이 상담 끝나는 시간을 힙에 넣음
                if min_time <= req[0]:
                    heappush(heap_n, req[0] + req[1])
                # 요청 시작 시간보다 크면 = 참가자가 기다렸다면 기다린 시간을 더하고 힙에 넣는다.
                else:
                    wait_time += min_time - req[0]
                    heappush(heap_n, min_time + req[1])

            # 첫 번째 반복 = 각각 상담원 수의 기본인 한명일 때 총 얼마나 기다리는 지 계산하기 위해 더함
            if n_ == 0:
                wait_init += wait_time
            # 상담원 이전 수(-1) 보다 단축한 시간을 wait_diff 에 넣어둠. 최대 힙
            else:
                heappush(wait_diff, wait_time - wait_k_)
            # 상담원 수 +1 했을 때와 비교하기 위해 wait_k_에 기다린 시간을 넣어둠
            wait_k_ = wait_time

    # 각각 한명일 때 총 기다린 시간
    wait_min = wait_init

    # 늘릴 수 있는 상담원 수만큼 반복하며 상담원이 늘 때 마다 가장 많이 줄이는 시간을 하나씩 빼며 계산
    # -> 각각 한명일 때 총 기다린 시간 - 모든 상담 중 상담원이 한명 늘어날 때 마다 가장 많이 줄어든 시간
    # 최대 힙 이므로 음수로 저장되어 있음
    for _ in range(max_n):
        wait_min += heappop(wait_diff)

    return wait_min