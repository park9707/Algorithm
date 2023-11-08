import sys
input = sys.stdin.readline


def main():
    dp_max = [0, 0, 0]
    dp_min = [0, 0, 0]

    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        dp_max[0] = (pre_a := max(dp_max[0], dp_max[1])) + a
        dp_max[2] = (pre_b := max(dp_max[1], dp_max[2])) + c
        dp_max[1] = max(pre_a, pre_b) + b

        dp_min[0] = (pre_a := min(dp_min[0], dp_min[1])) + a
        dp_min[2] = (pre_b := min(dp_min[1], dp_min[2])) + c
        dp_min[1] = min(pre_a, pre_b) + b

    print(max(dp_max), min(dp_min))


if __name__ == "__main__":
    main()