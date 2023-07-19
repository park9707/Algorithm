def dfs(arr, n, row):
    if n == row:
        return 1
    cnt = 0

    for i in range(n):
        arr[row] = i

        for j in range(row):
            if arr[j] == arr[row]:
                break
            elif abs(arr[row] - arr[j]) == row - j:
                break
        else:
            cnt += dfs(arr, n, row + 1)

    return cnt


def solution(n):
    arr = [0] * n
    return dfs(arr, n, 0)
