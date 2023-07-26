import collections, itertools

def make_info(info):
    dic = collections.defaultdict(list)
    case = list(itertools.product((True, False), repeat=4))
    for inf in info:
        inf = inf.split()
        for c in case:
            temp = ''.join([inf[i] if c[i] else '-' for i in range(4)])
            dic[temp].append(int(inf[4]))
    return dic


def find(dic, query):
    result = []
    for q in query:
        language, _, group, _, career, _, food, score = q.split()
        key = ''.join([language, group, career, food])
        result.append(binary_search(dic[key], int(score)))

    return result


def binary_search(arr, score):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < score:
            left = mid + 1
        else:
            right = mid
    return len(arr) - left


def solution(info, query):
    dic = make_info(info)
    for d in dic:
        dic[d].sort()

    return find(dic, query)
