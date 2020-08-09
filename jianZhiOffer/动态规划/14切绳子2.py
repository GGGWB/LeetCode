class Solution:
	def cuttingRope(self, n: int) -> int:
		memo = [i for i in range(n+1)]
		for i in range(1,n+1):
			for j in range(1,i//2+1):
				if memo[j]*memo[i-j]>memo[i]:
					memo[i] = memo[j]*memo[i-j] # 总体思想还是切第一刀的时候有哪些切法，然后从小到大计算，防止冗余计算
		
		if n<=3:
			return int(memo[n]-1)   #因为小于等于3的时候需要切割一下，不能不切所以和切割完剩下3或者2米的时候不一样
		else:
			return memo[n]%1000000007