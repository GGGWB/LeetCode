from math import sqrt
def num_color(n, m):
	min_color = float('inf')
	if m%2 == 0 or n%2 == 0:
		return 2
	else:
		for i in [n, m]:
			x = is_su(i)
			min_color = min(min_color, x)
		return min_color
def is_su(x):
	for i in range(2, int(sqrt(x))):
		if x % i == 0:
			return i
	return x
n = int(input())
ll = []
for i in range(n):
	l = list(map(int, input().strip().split()))
	ll.append(l)
for l in ll:
	m, n = l[0], l[1]
	x = num_color(m, n)
	print(x)