import sys
def method(ll, n, m):
    flag = [True] * n
    for i in ll:
        if i[0]==1:
            flag[i[1]-1]=False
        else:
            if flag[i[1]-1] == True:
                print(i[1])
            elif flag[i[1]]==True:
                print(i[1]+1)
            else:
                print(-1)

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
print(ll)
method(ll, n, m)