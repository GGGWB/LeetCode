class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(start, end):
            res = []
            if start > end:
                return [None]
            for idx in range(start, end+1):
                left_tree = helper(start, idx-1)
                right_tree = helper(idx+1, end)
                for l in left_tree:
                    for r in right_tree:
                        root = TreeNode(idx)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        return helper(1, n) if n else []


# 递归的方法，通过取其中一个值作为根， 左右的用来和原函数一样创建子树，然后处理节点，生成完整的树。