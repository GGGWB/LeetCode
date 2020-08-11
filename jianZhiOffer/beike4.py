def max_sum(l, a):
	n, m, k, d = a[0], a[1], a[2], a[3]
	raw_sum_list = []
	col_sum_list = [0 for _ in range(m)]
	for i in l:
		raw_sum = sum(i)
		raw_sum_list.append(raw_sum)
	for j in l:
		col_sum_list = [o+p for o, p in zip(j, col_sum_list)]
	raw_sum_list.sort()
	raw_sum_list.reverse()
	col_sum_list.sort()
	col_sum_list.reverse()
	if n<=m:
		l = []
		for i in range(n):
			sumi = 0
			for j in range(i):
				sumi += raw_sum_list[j]
			for p in range(k-i):
				sumi += col_sum_list[p]
			sumi -= d*i*(k-i)
			l.append(sumi)
		l.sort()
		return l[-1]
	else:
		l = []
		for i in range(m):
			sumi = 0
			for j in range(i):
				sumi += col_sum_list[j]
			for p in range(k-i):
				sumi += raw_sum_list[p]
			sumi -= d*i*(k-i)
			l.append(sumi)
		l.sort()
		return l[-1]
l = []
a = list(map(int, input().strip().split()))
while True:
	listi = list(map(int, input().strip().split()))
	if not listi:
		break
	l.append(listi)
ans = max_sum(l, a)
print(ans)

这道题还得改
		








#
# a = [1, 2, 3, 5, 4]
# b = [2, 3, 4]
# a.sort()
# a.reverse()
# # print([i+j for i, j in zip(a, b)])
# print(a)