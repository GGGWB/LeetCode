class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def oneSideMax(node):
            nonlocal ans
            if not node:
                return 0
            left = max(oneSideMax(node.left), 0)
            right = max(oneSideMax(node.right), 0)
            ans = max(ans, node.val + left + right)
            return node.val + max(left, right)
        ans = float('-inf')
        oneSideMax(root)
        return ans
