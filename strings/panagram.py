str = input().strip().replace(' ', '').lower()

arr = [0 for i in range(26)]

for c in str:
    arr[ord(c) - ord('a')] = 1

is_panagram = True
for i in arr:
    if i == 0:
        is_panagram = False
        break

if is_panagram:
    print('panagram')
else:
    print('not panagram')
