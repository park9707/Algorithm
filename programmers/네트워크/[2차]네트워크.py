def find(x, parent):
    if x == parent[x]:
        return x
    return find(parent[x], parent)


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif computers[i][j] == 1 and parent[i] != parent[j]:
                union(i, j, parent)

    answer = set()
    for i in range(n):
        answer.add(find(i, parent))

    return len(answer)
