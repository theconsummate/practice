N = int(input().strip())


def find_substr(a, b):
    found = False
    for c in a:
        index = b.find(c)
        if not index == -1:
            found = True
    if found:
        print('YES')
    else:
        print('NO')

for n in range(N):
    a = input().strip()
    b = input().strip()
    find_substr(a, b)
