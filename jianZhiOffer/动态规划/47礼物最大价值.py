class Solution:
	def maxValue(self, grid: List[List[int]]) -> int:
		# n = len(grid)
		# m = len(grid[0])
		# if n==1 and m==1:
		#     return grid[0][0]
		# elif n==1 or m==1:
		#     return sum(map(sum, grid))
		# dp = [[0 for _ in range(m)] for _ in range(n)]
		# dp[0][0] = grid[0][0]
		# for i in range(n):
		#     for j in range(m):
		#         if i == 0 and j > 0:
		#             dp[i][j] = dp[i][j-1] + grid[i][j]
		#         if i > 0 and j== 0:
		#             dp[i][j] = dp[i-1][j] + grid[i][j]
		#         else:
		#             dp[i][j] = max(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
		# return dp[n-1][m-1]
		m, n = len(grid), len(grid[0])
		for i in range(1, m):
			grid[i][0] += grid[i-1][0]
		for i in range(1, n):
			grid[0][i] += grid[0][i-1]
		for i in range(1, m):
			for j in range(1, n):
				grid[i][j] += max(grid[i-1][j], grid[i][j-1])
		return grid[-1][-1]