def solution(numbers, target):
    answer = 0
    n = len(numbers) - 1

    def dfs(r, i):
        nonlocal answer
        r_p = r + numbers[i]
        r_m = r - numbers[i]

        if i < n:
            dfs(r_p, i + 1)
            dfs(r_m, i + 1)

        elif i == n:
            if r_p == target or r_m == target:
                answer += 1

    dfs(0, 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))  # 2