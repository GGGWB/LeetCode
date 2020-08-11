# class Node:
# 	def __init__(self,data=None,next = None):
# 		self.data = data
# 		self.next = next
# def reverseList(head):
# 	"""
# 	:type head: ListNode
# 	:rtype: ListNode
# 	"""
# 	if not head or not head.next:
# 		return head
# 	Node = None
# 	while head:
# 		p = head
# 		head = head.next
# 		p.next = Node
# 		Node = p
# 	return Node
# link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
# root = reverseList(link)
# while root:
# 	print(root.data)
# 	root =root.next
import  random as rd

class Linklist(object):
	def __init__(self,data,next=None):
		self.data=data
		self.next=next

def createListHead(n):
	L=Linklist(0)  ##链表头
	list=[]
	for i  in range(n):
		num=rd.randint(0,100)
		list.append(num)
		p=Linklist(num,L.next)
		L.next=p
		L.data+=1 ##链表长度加1
	print("rawlist===",list)
	return L

def createListTail(n):
	
	L=Linklist(0)  ##链表头
	list = []
	
	num = rd.randint(0, 100)
	list.append(num)
	head=Linklist(num)  ##建立实际数据表头
	L.data+=1 ##链表长度加1
	
	L.next=head
	temp=head ##建立当前数据指针
	for i  in range(n-1):
		num = rd.randint(0, 100)
		list.append(num)
		p=Linklist(num)
		temp.next=p ##当前数据的指针指向新数据
		temp=p  ##移动当前数据指针
		L.data+=1 ##链表长度加1
	temp.next=None
	print('raw data',list)
	return L

if __name__=='__main__':
	head=createListTail(10)
	
	realData=head.next
	list = []
	while realData!=None:
		list.append(realData.data)
		realData=realData.next
	print('linklist===',list)
	print('linklist len====',head.data)