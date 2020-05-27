import sys
def method(n, a):
    flag = [False] * n
    for i in range(n-1):
        while True:
            ref = 1
            try:
                b = bin(a[i+ref])[1:-2]
                c = bin(a[i])[1:-2]
                for i in b:
                if b & c == 0:
                    flag[i], flag[i+ref] = True, True
                ref += 1
            except:
                break
    return flag

ll = []
n=int(input())
a = list(map(int, input().split()))
print(a)
flag = method(n, a)
for i in flag:
    if i == True:
        print(1)
    else:
        print(-1)