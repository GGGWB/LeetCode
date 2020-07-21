def method(n):
	if n == 1:
		return 1
	return n*method(n-1)
a = method(5)
print(a)