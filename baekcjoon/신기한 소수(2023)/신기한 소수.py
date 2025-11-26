import sys
input = sys.stdin.readline


def is_prime_num(x):
    for num in range(2, int(x ** 0.5) + 1):
        if x % num == 0:
            return False
    return True


n = int(input())
prime_nums = [2, 3, 5, 7]
for _ in range(n - 1):
    new_prime_nums = []
    for p in prime_nums:
        for i in range(1, 10, 2):
            k = int(p * 10 + i)
            if is_prime_num(k):
                new_prime_nums.append(k)

    prime_nums = new_prime_nums

for p in prime_nums:
    print(p)
