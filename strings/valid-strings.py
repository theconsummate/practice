# https://www.hackerrank.com/challenges/sherlock-and-valid-string
import sys
str = input().strip().replace(' ', '').lower()

arr = [0 for i in range(26)]

freq = {}
for c in str:
    if c in freq:
        # increase by 1
        freq[c] += 1
    else:
        # init to 1
        freq[c] = 1

diff = 0
prev = 0
can_modify = True
is_valid = True
# {'c': 1, 'b': 2, 'a': 2, 'd': 1}
for key in freq:
    if prev == 0:
        prev = freq[key]
    elif not freq[key] == prev:
        prev = freq[key]
        is_valid = False
    if not diff == 0 and diff - freq[key] > 1:
        can_modify = False
        break
    else:
        diff += freq[key]

if is_valid:
    print('YES')
    sys.exit()
if can_modify:
    print('YES')
else:
    print('NO')
