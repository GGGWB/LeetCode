import sys




data = []
while 1:
	line = sys.stdin.readline().strip()
	if not line:
		break
	line = list(map(int, line.split()))
	data.append(line)
x = data.pop(0)
n, m = x[0], x[1]
print(n, m)
new = [[0 for i in range(m+2)] for j in range(n+2)]
for i in range(1, n+1):
	for j in range(1, m+1):
		new[i][j] = data[i-1][j-1]
print(new)