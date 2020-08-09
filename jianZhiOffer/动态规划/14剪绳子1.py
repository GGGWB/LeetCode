class Solution:
	def cuttingRope(self, n: int) -> int:
		if n < 2:
			return 0
		if n==2:
			return 1
		if n==3:
			return 2
		product = [0 for _ in range(n+1)]
		product[0] = 0
		product[1] = 1
		product[2] = 2
		product[3] = 3 # 这个地方和最上面的初始化状态不能混为一谈，因为上面是要裁剪得到的答案，这里是给出了裁剪完后的最后状态
		maxs = 0
		for i in range(4, n+1):
			maxs = 0
			for j in range(1, int(n/2)+1):
				leng = product[i-j]*product[j]
				if maxs < leng:
					maxs = leng
			product[i] = maxs
		return product[n]