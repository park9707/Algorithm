import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards_idx = {card: idx for idx, card in enumerate(cards, 1)}
score = [0] * N
max_num = max(cards)

for i in range(N):
    num = cards[i]
    for j in range(num + num, max_num + 1, num):
        if cards_idx.get(j, 0):
            score[i] += 1
            score[cards_idx[j] - 1] -= 1

print(*score)
