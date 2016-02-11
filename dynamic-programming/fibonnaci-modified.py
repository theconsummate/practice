# https://www.hackerrank.com/challenges/fibonacci-modified
a, b, n = input().strip().split(' ')
a = int(a)
b = int(b)
n = int(n)

arr = [a, b]
temp = [-1 for i in range(n - 2)]
arr.extend(temp)

for i in range(2, n):
    arr[i] = arr[i - 1]**2 + arr[i - 2]

print(arr[-1])
