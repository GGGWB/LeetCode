# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		reversed_head = None
		cnode = head
		pnode = None  # 剑指上的讲解非常清晰，只需看一次就行
		# 重点在图，为防止链表翻转断裂对于当前节点需要知道前后节点，所以要定义个前面节点，然后在循环过程中记下之后节点
		while cnode is not None:
			nnode = cnode.next
			if nnode is None:
				reversed_head = cnode
			cnode.next = pnode
			pnode = cnode
			cnode = nnode
		return reversed_head

