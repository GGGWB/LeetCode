import sys
def num(value, n):
	x = 0
	ref = 0
	for i in range(n+1):
		if i == n:
			x += int((ref)/2)
			return x
		if value[i] == 0:
			ref += 1
		if value[i] == 1:
			x += int((ref-1)/2)
			ref = 0
n = int(input())
line = sys.stdin.readline().strip()
line = list(map(int, line.split()))
a = num(line, n)
print(a)


import sys
def num(value, n):
	x = 0
	ref = 0
	flag = 0
	for i in range(n+1):
		if i == n:
			x += int(ref/2)
			return x
		if value[0] == 1:
			flag = 1
		if value[i] == 0:
			ref += 1
		if value[i] == 1 and flag == 0:
			x += int(ref/2)
			flag = 1
			ref = 0
		elif value[i] == 1:
			x += int((ref-1)/2)
			ref = 0
n = int(input())
line = sys.stdin.readline().strip()
line = list(map(int, line.split()))
a = num(line, n)
print(a)