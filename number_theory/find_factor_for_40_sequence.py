# Enter your code here. Read input from STDIN. Print output to STDOUT
# find Y such that xy is a series of 4 followed by a one or more 0's
# 404 is invalid but 4400 400 etc are all valid.
# input: first line is number of test cases
# after than each line contains an X for which Y has to be found as per the constraint above
# in the number XY, let "a" be the count of 4's and "b" be the count 0's
# return 2a + b for each input test case


def calc(n):
    num_factors_of_5 = 0
    num_factors_of_2 = 0
    # trivial case 0 result is 0
    if n==0:
        return 0

    # calculate factors of 5
    temp = n
    while temp > 0:
        if temp%5 == 0:
            temp /=5
            num_factors_of_5 += 1
        else:
            break

    # calculate factor of 2
    temp = n
    while temp > 0:
        if temp%2 == 0:
            temp /=2
            num_factors_of_2 += 1
        else:
            break


    t1 = num_factors_of_5
    if t1 < (num_factors_of_2 - 2):
        t1 = num_factors_of_2 -2

    a = 4
    for i in range(t1):
        a *= 10

    b = 1
    while not (a*b)%n == 0:
        b = 10*b + 1

    return a*b


def print_output(num):
    a = 0
    b = 0
    for i in str(num):
        if i == '4':
            a += 1
        elif i == '0':
            b += 1
    print 2*a + b


t = int(raw_input())
for i in range(0,t):
    x = int(raw_input())
    print_output(calc(x))
