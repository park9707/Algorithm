def solution(skill, skill_trees):
    dic = dict()
    answer = 0
    for i, s in enumerate(skill):
        dic[s] = i

    for a in skill_trees:
        tmp = 0
        for i in a:
            if i in dic:
                if dic[i] == tmp:
                    tmp += 1
                else:
                    break
        else:
            answer += 1

    return answer
