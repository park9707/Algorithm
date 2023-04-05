def solution(plans):
    answer, stack = [], []
    plans.sort(key=lambda x: x[1])

    for subject, start, time in plans:
        h, m = map(int, start.split(':'))
        start = 60 * h + m  # 시간을 초로 변경
        time = int(time)

        if stack:  # 스택이 비어있지 않다면
            pre_subject, pre_start, pre_time = stack.pop()  # 과목, 시작 시간, 걸리는 시간 스택에서 빼냄
            time_term = start - pre_start  # 현재 과목 시간과 스택에서 가져온 과목 시작 시간 차이

            if time_term < pre_time:  # 시간 차이가 이전 과목 걸리는 시간보다 작다면
                stack.append((pre_subject, pre_start, pre_time - time_term))  # 한 시간만큼 빼고 스택에 다시 넣음
            else:  # 시간 차이가 이전 과목 걸리는 시간보다 더 크다면
                answer.append(pre_subject)  # 이전 과목은 끝냄
                time_term = time_term - pre_time  # 시간 차이에서 걸린 시간 빼기

                while stack and time_term:  # 스택이 비어있지 않고, 사용할 수 있는 시간이 남아있다면 반복
                    pre_subject, pre_start, pre_time = stack.pop()  # 과목 하나 빼냄

                    if time_term < pre_time:  # 시간 차이가 이전 과목 걸리는 시간보다 작다면
                        stack.append((pre_subject, pre_start, pre_time - time_term))  # 한 시간만큼 빼고 스택에 다시 넣고 break
                        break
                    else:  # 시간 차이가 이전 과목 걸리는 시간보다 더 크다면
                        answer.append(pre_subject)  # 과목을 끝냄
                        time_term = time_term - pre_time  # 시간 차이에서 걸린 시간 빼기

        stack.append((subject, start, time))

    answer.extend([sub for sub, st, ti in stack[::-1]])  # 스택에서 뒤쪽부터 하나씩 빼냄
    return answer

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))