# def get_k(n):
# 	ten = [i for i in range(1, 11)]
# 	if n in ten:
# 		if n ==1:
# 			return 1
# 		elif n==2 or n==3:
# 			return 2
# 		elif n>3 and n<8:
# 			return 3
# 		elif n>7:
# 			return 4
# 	x = 0
# 	while True:
# 		if 2**x * 20 >= n:
# 			return x+5
# 		x += 1
# 		continue
def get_k(n):
	# ten = [i for i in range(1, 11)]
	# if n in ten:
	# 	if n ==1:
	# 		return 1
	# 	elif n==2 or n==3:
	# 		return 2
	# 	elif n>3 and n<8:
	# 		return 3
	# 	elif n>7:
	# 		return 4
	x = 0
	while True:
		n = n-2**x
		if n <= 2**(x+1):
			return x+2
		else:
			x+=1
# n = int(input())
# l = []
# for i in range(n):
# 	x = int(input())
# 	l.append(x)
# for i in l:
# 	a = get_k(i)
# 	print(a)
#
#
a = get_k(9)
print(a)

# n = int(input())
# l = []
# for i in range(n):
# 	x = int(input())
# 	l.append(x)
# for i in l:
# 	a = get_k(i)
# 	print(a)
