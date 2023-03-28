from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    for i in permutations(user_id, len(banned_id)):
        cnt = 0
        for user, ban in zip(i, banned_id):
            check = True
            if len(user) != len(ban):
                break
            else:
                for j in range(len(user)):
                    if ban[j] == '*':
                        continue
                    elif ban[j] != user[j]:
                        check = False
                        break
                if check:
                    cnt += 1
                else:
                    break
        else:
            if sorted(i) not in answer:
                answer.append(sorted(i))
    return len(answer)
