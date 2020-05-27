import sys
import copy
def count_num(ll, n, m):
    flag = [False] * n
    for i in range(m):
        new = []
        for j in range(n):
            new.append(ll[j][i])
        b = copy.deepcopy(new)
        b.sort()
        x = b.pop()
        while True:
            try:
                a = new.index(x)
                flag[a] = True
                new[a] += 1
            except:
                break
    res = 0
    for i in flag:
        if i == True:
            res += 1
    return res

ll = []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    line = list(map(int, line.split()))
    ll.append(line)
n = ll[0][0]
m = ll[0][1]
ll.pop(0)
res = count_num(ll, n, m)
print(res)