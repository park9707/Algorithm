def solution(triangle):
    for i in range(len(triangle)-2, 0, -1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0] + max(triangle[1])
