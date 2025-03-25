import math


def solution(n, bans):
    answer = ''
    bans.sort(key=lambda x: (len(x), x))
    nums = {chr(97 + i): i + 1 for i in range(26)}
    chars = {i + 1: chr(97 + i) for i in range(25)}
    chars[0] = 'z'
    digit = int(math.log(n, 26)) + 1
    l, r = 0, len(bans) - 1
    while l < r:
        mid = (l + r) // 2
        if len(bans[mid]) >= digit:
            num = 0
            for i, c in enumerate(reversed(bans[mid])):
                num += (26 ** i) * nums[c]
            if n + l < num:
                r = mid
            elif n + l > num:
                l = mid + 1
            else:
                l = mid
                break
        elif len(bans[mid]) < digit:
            l = mid + 1
    n += l
    r = len(bans)
    while l < r:
        num = 0
        for i, c in enumerate(reversed(bans[l])):
            num += (26 ** i) * nums[c]
        if num <= n:
            l += 1
            n += 1
        else:
            break

    for _ in range(digit):
        answer += chars[n % 26]
        if n % 26 == 0:
            n -= 1
        n //= 26
    return answer[::-1]
