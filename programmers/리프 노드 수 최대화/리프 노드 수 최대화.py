def dfs(tree, dist_limit, split_limit):
    global ans
    if dist_limit < 0:
        return

    pre_node = tree[-1]
    current_node = pre_node[0] * pre_node[1]
    for i in (2, 3):
        if current_node * i <= split_limit:
            if pre_node[1] > i:
                continue

            ans = max(ans, current_node + (min(dist_limit, current_node) * (i - 1)))
            dfs(tree + [[current_node, i]], dist_limit - current_node, split_limit)


def solution(dist_limit, split_limit):
    global ans
    ans = 1
    dfs([[1, 1]], dist_limit, split_limit)
    return ans


# print(solution(12, 24)) - 반례
# 다른 풀이 봤을 때도 전부 18로 나오지만 답은 19가 나와야 함
