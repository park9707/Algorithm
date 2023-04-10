def solution(sequence, k):
    answer = []
    n = len(sequence) - 1
    l = r = 0
    v = sequence[0]
    while l <= r < n:
        while v < k:
            r += 1
            v += sequence[r]
        while v > k:
            v -= sequence[l]
            l += 1
        if v == k:
            answer.append([l, r])
            v -= sequence[l]
            l += 1

    return sorted(answer, key=lambda x: x[1]-x[0])[0]
