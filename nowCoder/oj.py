import sys
a, b = [], []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    line = list(map(int, line.split()))
    a.append(line[0])
    b.append(line[1])
for i in range(len(a)):
    print(a[i]+b[i])
# 1 5
# 10 20
import sys
ll = []
n = int(input())
for i in range(n):
    line = sys.stdin.readline().strip()
    if not line:
        break
    line = list(map(int, line.split()))
    ll.append(line)
for i in range(len(ll)):
    print(ll[i][0]+ll[i][1])
# 2
# 1 5
# 10 20
import sys
ll = []
while True:
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    ll.append(line)
    if line[0] == 0 and line[1] == 0:
        break
for i in range(len(ll)-1):
    print(ll[i][0]+ll[i][1])
# 1 5
# 10 20
# 0 0
import sys
ll = []
while True:
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    ll.append(line)
    if line[0] == 0:
        break
for i in range(len(ll)-1):
    print(sum(ll[i])-ll[i][0])
# 4 1 2 3 4
# 5 1 2 3 4 5
# 0