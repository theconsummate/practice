# https://www.hackerrank.com/challenges/maxsubarray


# max sum of subsequences
def maxSubsequenceSum(a):
    sum_subsequence = 0
    max_neg = -10000
    for n in a:
        if n > 0:
            sum_subsequence += n
        elif n > max_neg:
            max_neg = n

    if sum_subsequence == 0:
        sum_subsequence = max_neg

    return sum_subsequence


# kadane algorigthm
def maxSubArraySum(a):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, len(a)):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

T = int(input().strip())
# arr = []
for t in range(T):
    N = int(input().strip())
    arr = [int(num) for num in input().strip().split(' ')]
    print(maxSubArraySum(arr), maxSubsequenceSum(arr))
