def cost_for_twos(depth, target_frontier):
    total_cost = 0
    for level in range(1, depth + 1):
        total_cost += (target_frontier + (1 << level) - 1) // (1 << level)
    return total_cost


def solution(dist_limit, split_limit):
    answer = 1

    pow2 = 1
    num_two_layers = 0

    while pow2 <= split_limit:
        # 2분배만 쓰는 경우
        answer = max(answer, 1 + min(dist_limit, pow2 - 1))

        pow3 = 3

        while pow2 * pow3 <= split_limit:
            # 3분배 전체를 채우는데 필요한 비용 계수
            cost_per_frontier_3 = (pow3 - 1) // 2

            max_frontier = pow2
            max_two_nodes = pow2 - 1

            candidates = {0, 1, max_frontier}

            # 후보 1: 2분배만으로 만들 수 있는 최대 frontier
            lo, hi = 0, max_frontier
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if cost_for_twos(num_two_layers, mid) <= dist_limit:
                    lo = mid
                else:
                    hi = mid - 1

            for x in range(lo - 5, lo + 6):
                candidates.add(x)

            # 후보 2: 3분배까지 포함하면 예산 넘는 지점
            lo, hi = 0, max_frontier
            while lo < hi:
                mid = (lo + hi) // 2
                if cost_for_twos(num_two_layers, mid) + cost_per_frontier_3 * mid >= dist_limit:
                    hi = mid
                else:
                    lo = mid + 1

            for x in range(lo - 5, lo + 6):
                candidates.add(x)

            # 후보 3: 3분배까지 딱 채울 수 있는 최대 지점
            lo, hi = 0, max_frontier
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if cost_for_twos(num_two_layers, mid) + cost_per_frontier_3 * mid <= dist_limit:
                    lo = mid
                else:
                    hi = mid - 1

            for x in range(lo - 5, lo + 6):
                candidates.add(x)

            for frontier in candidates:
                if not (0 <= frontier <= max_frontier):
                    continue

                cost_two = cost_for_twos(num_two_layers, frontier)

                if cost_two > dist_limit:
                    continue

                # 3분배에 사용할 수 있는 개수
                cost_three = min(dist_limit - cost_two, cost_per_frontier_3 * frontier)

                # 남은 예산으로 다시 2분배
                extra_two = min(
                    dist_limit - cost_two - cost_three,
                    max_two_nodes - cost_two
                )

                leaf_count = 1 + cost_two + extra_two + cost_three * 2
                answer = max(answer, leaf_count)

            pow3 *= 3

        pow2 *= 2
        num_two_layers += 1

    return answer