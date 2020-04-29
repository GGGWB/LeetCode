class Solution:
    def numTrees(self, n: int) -> int:
        G = [0 for i in range(n+1)]
        G[0] = 1
        G[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1]*G[i-j]
        return G[n]

# 考虑这是个动态规划问题，
# 从二叉搜索树的性质入手，只要跟从中间分开，则左右两边内容如何排列不重要，重要的是结果
# 找到规律写出来，然后转换成代码

# 数学演绎法，根据G函数获取Gn+1和Gn之间的递推关系C_next=2（2n+1)/n+2*c_curr
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
