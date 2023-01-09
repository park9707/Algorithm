from itertools import permutations

def is_prime_num(num):
    if num == 2:
        return True

    if num == 0 or num == 1 or num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    split_nums = [i for i in numbers]
    nums = []
    for i in range(1, len(numbers)+1):
        nums.extend(list(permutations(split_nums, i)))

    join_nums = [int(''.join(i)) for i in nums]

    prime_nums = set()

    for i in join_nums:
        if is_prime_num(i):
            prime_nums.add(i)
    return len(prime_nums)