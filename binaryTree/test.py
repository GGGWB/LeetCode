class Tree:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
root = Tree(5, None, None)
a = [root,]
b = [root]
print(type(a[0]))
print(type(b[0]))
print(len(a))
print(len(b))
