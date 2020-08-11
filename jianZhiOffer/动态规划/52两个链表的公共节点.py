# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		def get_length(head):
			length = 0
			if head is None:
				return length
			while head is not None:
				head = head.next
				length += 1
			return length
		length1 = get_length(headA)
		length2 = get_length(headB)
		if length1>=length2:
			headLong, headShort = headA, headB
		else:
			headLong, headShort = headB, headA
		length_diff = abs(length1-length2)
		for i in range(length_diff):
			headLong = headLong.next
		while headLong is not None and headShort is not None:
			if headLong == headShort:  # 这个地方需要注意，不能只比较里面的值
				return headLong
			headLong,headShort = headLong.next, headShort.next
		return None