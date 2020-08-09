import sys
#str = input()
#print(str)
def method(arr):
	x = [[] for _ in range(101)]
	for i in arr:
		x[i].append(i)
	for j in range(100):
		if x[100-j] != [] and x[j]!=[] and  x[j][0] + x[100-j][0] ==100:
			return (j, 100-j)


a = [1, 23, 3, 4, 5, 6, 7, 8, 9, 23, 45, 67, 44, 33, 22, 88, 77, 67, 44, 33, 12, 88]
print(method(a))
