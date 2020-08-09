class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		n, m = len(s), len(p)
		dp = [[False] * (m+1) for _ in range(n+1)]
		for i in range(n+1):
			for j in range(m+1):
				if j==0: # 空正则
					dp[i][j] = i==0
				else:  # 非空正则
					if p[j-1] != '*': # 正则末尾不为*
						if i>0:
							if p[j-1] == s[i-1] or p[j-1] =='.':
								dp[i][j] = dp[i-1][j-1]
					else:  # 正则末尾为*
						if j>=2:
							dp[i][j] |= dp[i][j-2]
						if i>=1 and j>=2:
							if p[j-2] == s[i-1] or p[j-2] =='.':
								dp[i][j] |= dp[i-1][j]
		return dp[n][m]
# 关于为什么用|=，比如这段代码： //碰到 * 了，分为看和不看两种情况 //不看 if (j >= 2) { f[i][j] |= f[i][j - 2]; //可用可不用，因为dp矩阵初始化默认为false，本质上和=一样 } //看 if (i >= 1 && j >= 2 && (A.charAt(i - 1) == B.charAt(j - 2) || B.charAt(j - 2) == '.')) { f[i][j] |= f[i - 1][j]; //必须使用，否则不能ac }

# 其中，第一步先算的是不看‘*’的情况，然后第二步再算看‘*’的情况。也就是说，对于f[i][j]我们会算两次。如果在第一次，即不看'*'的时候，就已经算出来TURE了。那在第二步看'*'的时候。不管结果是ture还是false，都保持true不变，这是合理的，因为只要其中有一种情况能完整匹配，结果就为true。这就是为什么要用或符号。 这个不难证明，举个例子 "ba" "baa*" 这种情况下直接用=号过不了。