def time_min1(a, b):
	n = len(a)
	l = [0 for i in range(n)]
	def time_min(a, b, l):
		min_time = 0
		if n == 1:
			min_time = a[0]
			l[0] = min_time
		elif n ==2:
			min_time = min(a[0]+a[1], b[0])
			l[1] = min_time
		else:
			if l[n-1] != 0 and l[n-2] != 0:
				min_time = min(l[n-1]+a[n-1], l[n-2]+b[n-2])
			else:
				min_time = min(time_min(a[0:n-2], b, l)+b[n-2], a[n-1]+time_min(a[0:n-1], b, l))
		return min_time
	x = time_min(a, b, l)
	return x
	

n = int(input())

for i in range(n):
	p = int(input())
	a = list(map(int, input().strip().split()))
	b = list(map(int, input().strip().split()))
	x = time_min1(a, b)
	hour_nu = int(x/3600)
	mi = int((x - 3600*hour_nu)/60)
	sec = x - hour_nu*3600 - mi * 60
	ho = 8 + hour_nu
	print(str(0)+str(ho)+':'+'00'+':'+str(sec)+' '+'am')

