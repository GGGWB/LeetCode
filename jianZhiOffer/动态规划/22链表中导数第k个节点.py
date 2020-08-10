# # Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, data):
# 		self.val = data
# 		self.next = None
# a = [1, 2, 3, 4, 5, 6]
# b = ListNode(0)
# head = b
# for i in a[::-1]:
# 	x = ListNode(i)
# 	p = b.next
# 	b.next = x
# 	x.next = p
# while head is not None:
# 	print(head.val)
# 	head = head.next
class Solution:
	def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
		ahead = head
		bhead = head
		for i in range(k-1):     #剑指offer真的是牛皮啊
			if ahead.next is not None:
				ahead = ahead.next
			else:
				return None
		while(ahead.next is not None):
			ahead = ahead.next
			bhead = bhead.next
		return bhead
