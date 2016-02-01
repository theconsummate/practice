# https://www.hackerrank.com/challenges/almost-sorted
import sys
N = int(input().strip())
arr = [int(num) for num in input().strip().split(' ')]

anomalies = []

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        if len(anomalies) < 2 or (len(anomalies) > 0 and i - anomalies[-1] == 1):
            anomalies.append(i)
        else:
            print("no")
            sys.exit()

if not anomalies:
    print("yes")
    sys.exit()

print(anomalies)
size = len(anomalies)
left = anomalies[0]
right = anomalies[-1] + 1
keyword = "swap" if size <= 2 else "reverse"
if (left == 0 or arr[right] >= arr[left - 1]) and (right == N - 1 or arr[left] <= arr[right + 1]):
    print("yes\n" + keyword, left + 1, right + 1)
else:
    print("no\n")
    sys.exit()
