def time_min(a, b):
	n = len(a)
	min_time = 0
	if n == 1:
		min_time = a[0]
	elif n ==2:
		min_time = min(a[0]+a[1], b[0])
	else:
		min_time = min(time_min(a[0:n-2], b)+b[n-2], a[n-1]+time_min(a[0:n-1], b))
	return min_time

# a = [20, 25]
# b = [40]
n = int(input())
person = []
time1 = []
time2 = []
for i in range(n):
	p = int(input())
	person.append(p)
	a = list(map(int, input().strip().split()))
	time1.append(a)
	b = list(map(int, input().strip().split()))
	time2.append(b)

for i in range(n):
	x = time_min(time1[i], time2[i])
	hour_nu = int(x/3600)
	mi = int((x - 3600*hour_nu)/60)
	sec = x - hour_nu*3600 - mi * 60
	ho = 8 + hour_nu
	print(str(0)+str(ho)+':'+'00'+':'+str(sec)+' '+'am')

