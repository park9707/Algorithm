from itertools import product


def solution(users, emoticons):
    answer = []
    m = len(emoticons)
    for discounts in product((10, 20, 30, 40), repeat=m):
        temp = [0, 0]

        for user_discount, user_price in users:
            total_amount = 0

            for d, e in zip(discounts, emoticons):
                if user_discount <= d:
                    total_amount += e * (1 - d / 100)

            if user_price <= total_amount:
                temp[0] += 1
            else:
                temp[1] += int(total_amount)

        answer.append(temp)

    return sorted(answer, key=lambda x: (x[0], x[1]), reverse=True)[0]
