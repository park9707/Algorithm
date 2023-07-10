from sys import stdin
input = stdin.readline

n, k = map(int, input().rstrip().split(' '))
weights = [0] * n
values = [0] * n
for i in range(n):
    weights[i], values[i] = map(int, input().rstrip().split(' '))

knapsack = {0: 0}
for t_w, t_v in zip(weights, values):
    tmp = dict()
    for k_v, k_w in knapsack.items():
        if knapsack.get(n_v := t_v + k_v, k + 1) > (n_w := t_w + k_w):
            tmp[n_v] = n_w
    knapsack.update(tmp)

print(max(knapsack.keys()))
