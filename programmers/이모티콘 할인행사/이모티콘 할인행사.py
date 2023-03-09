from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    for discounts in product((10, 20, 30, 40), repeat=len(emoticons)):  # 나올 수 있는 할인 조합들
        sold = [0, 0]  # 가입 수, 판매액
        for user_discount, user_price in users:
            total_price = 0
            for discount, emoticon in zip(discounts, emoticons):  # 할인율과 이모티콘 가격 하나씩 조합
                if user_discount <= discount:  # 할인율이 유저의 구매 희망 할인율보다 높다면
                    total_price += emoticon * (1 - discount / 100)  # 이모티콘 할인가
            if total_price >= user_price:  # 총 금액이 일정 가격 이상이 된다면
                sold[0] += 1  # 이모티콘 플러스 서비스 가입
            else:
                sold[1] += int(total_price)  # 이모티콘 판매액 더하기
        answer = max(answer, sold)

    return answer
