# T = int(input().strip())


def sum_natural_num(n):
    n = int(n)
    return n * (n + 1) * (1 / 2)


def find_sum_of3_and5(N):
    # https://www.hackerrank.com/contests/projecteuler/challenges/euler001
    N = N - 1
    return 3 * sum_natural_num(N / 3) + 5 * sum_natural_num(N / 5) - 15 * sum_natural_num(N / 15)

# for t in range(T):
#     N = int(input().strip())
#     print(find_sum(N))
N = 10
# int(input().strip())
print(find_sum_of3_and5(N))
