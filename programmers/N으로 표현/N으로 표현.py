def solution(N, number):
    dp = []

    for i in range(1, 9):   # 최대 8개 까지
        all_case = set()
        check_number = int(str(N) * i)  # N, NN , NNN, ...
        all_case.add(check_number)

        for j in range(0, i - 1):   # i를 둘로 나눠서 계산
            for op1 in dp[j]:   # j번째와
                for op2 in dp[-j - 1]:  # 뒤에서 j+1 번째 값 하나씩 계산
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)

        if number in all_case:  # 타겟이 들어있다면 리턴
            return i

        dp.append(all_case)

    return -1
