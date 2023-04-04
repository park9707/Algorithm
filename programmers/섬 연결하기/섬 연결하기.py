def find(parents, n):
    if n != parents[n]:
        return find(parents, parents[n])
    return n


def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]

    costs.sort(key=lambda x: x[2])

    for cost in costs:
        if find(parents, cost[0]) != find(parents, cost[1]):
            union(parents, cost[0], cost[1])
            answer += cost[2]

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))