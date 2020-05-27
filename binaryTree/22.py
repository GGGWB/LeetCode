import copy
def hanmin(a, b):
    res = 0
    m = int(bin(a)[2:])
    n = int(bin(b)[2:])
    print(m, n)
    print(str(abs(m+n)))
    for i in str(abs(m+n)):
        print('idezhi{}'.format(i))
        if i == '1':
            res += 1
    return res
n = int(input())
line = list(map(int, input().split()))
max1 = 0
for i in line:
    for x in line:
        length = hanmin(x, i)
        print('length{}'.format(length))
        max1 = length if length > max1 else max1
print(max1)