class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class solution():
	def reverseList(self, head:Node) -> Node:
		if head is None:
			return None
		curhead = Node(head.data)
		prehead = head.next
		while prehead is not None:
			tmp = prehead.next
			prehead.next = curhead
			curhead = prehead
			prehead = tmp
		return curhead
		
if __name__ == "__main__":
	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)
	e = Node(5)
	a.next = b
	b.next = c
	c.next = d
	d.next = e
	method = solution()
	a = method.reverseList(a)
	while a is not None:
		print(a.data)
		a = a.next