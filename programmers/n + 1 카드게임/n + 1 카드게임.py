def solution(coin, cards):
    answer = 1
    n = len(cards)
    my_card = dict()
    pending = dict()
    r = tmp_r = 0
    for c in cards[:n // 3]:
        if my_card.get(n - c + 1):
            r += 1
            continue
        my_card[c] = True

    for i in range(n // 3, n, 2):
        if coin <= 0:
            r += coin
            break
        a, b = cards[i:i + 2]

        if my_card.get(n - a + 1):
            coin -= 1
            r += 1
        elif pending.get(n - a + 1):
            tmp_r += 1
        else:
            pending[a] = True

        if my_card.get(n - b + 1):
            coin -= 1
            r += 1
        elif pending.get(n - b + 1):
            tmp_r += 1
        else:
            pending[b] = True

        if r == 0:
            if tmp_r >= 1 and coin >= 2:
                coin -= 2
                tmp_r -= 1
                r += 1
            else:
                break
        r -= 1
        answer += 1

    return answer + r