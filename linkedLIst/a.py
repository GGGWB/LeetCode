class Node:
	def __init__(self,data=None,next = None):
		self.data = data
		self.next = next
def reverseList(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	if not head or not head.next:
		return head
	Node = None
	while head:
		p = head
		head = head.next
		p.next = Node
		Node = p
	return Node
link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
root = reverseList(link)
while root:
	print(root.data)
	root =root.next