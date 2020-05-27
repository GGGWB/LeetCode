import time
import calendar
a = time.time()
b = time.localtime(a)
c = time.asctime(b)
print(a, '\n')
print(b)
print(c)
e = calendar.month(1995, 11)
print(e)

def max_height(n, m, x):
    a = int(n*(n-1)/2)
    if a<m:
        level = (m-a)//n
        p = m - n*level
        o = p-a
        if o>=(n-x):
            return level+n-x+1
        else:
            return level+n-x
    else:
        u = a-m
        return n-x+1