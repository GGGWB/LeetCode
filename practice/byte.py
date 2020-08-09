def count_max(a):
	ref = 0
	for i in a:
		if i > 1:
			count_2 = int(i/2)
			ref = ref + count_2
	return ref

n = int(input())
a = list(map(int, input().split()))
num = count_max(a)
print(num)

	