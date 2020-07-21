#
# 判断N是否可由2、5、7相乘得到，如果可以，返回1，否则返回0
# @param N int整型 乘积
# @return int整型
#

def is_product(N):
	print(N)
	# write code here
	while N % 2 == 0: # 化为奇数,个位是 1， 3， 5， 7 ,9
		N /= 2
	while N % 5==0: # 去除5的干扰,个位是1， 3，
		N /= 5
	while N % 7==0:
		N /= 7
	if N == 1:
		print('行')
		print('   ')
		return
	else:
		print(N)
		print('   ')
		return
for i in range(1, 1000):
	is_product(i)
