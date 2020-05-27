# import sys

# line = input().strip()
# num = (len(line)-line.count(' '))/(line.count(' ')+1)
# print('%.2f' % num)
# v = 3 + 4j
# a = -1000.0010000
# print(abs(a))
# a = any([0, ' ', False])
#
# print(a)
# print(ascii((1,2))) #元组
# print(type(ascii((1,2))))
#
# print(ascii([1,2])) #列表
# print(type(ascii([1,2])))
#
# print(ascii({1:2,'name':5})) #字典
# print(type(ascii({1:2,'name':5})))
#
# print(ascii('??')) #字符串，非 ASCII字符，转义
# print(type(ascii("?")))
# a = list((1,1,2,3))
# print(ascii(set(a))) #集合，由set()创建
# print(type(ascii(a)))
# print(repr(a))
# print(str(a))
# print(repr(a)==str(a))
# a ={'a': 'a', 'b': 'b', 'c': '3'}
# b =  dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# print(b)
# b = [1, 2 , '3', 4,5, 6,7,8,8, 9, 3,3,3,3,33]
# x = b.popitem(1)
# print(x)
# a = b.count(3)
# print(a)
# a = dir([])
# print(a[-11:])
# seq = ['one', 'two', 'three']
# for i, element in enumerate(seq):
# 	print(i, element)
# site = {"name": "菜鸟教程", "url": "www.runoob.com"}
# print("网站名：{name}, 地址 {url}".format(**site))
# a = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
# print(a)
class ListNode():
	def __init__(self, elem):
		self.elem = elem
		self.next = None

def hasCycle(List):
	slow = fast = node1
	
	while fast.next.next and slow.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True
	return False

if __name__ =="__main__":
	node1 = ListNode(1)
	node2 = ListNode(2)
	node3 = ListNode(3)
	node4 = ListNode(4)
	node5 = ListNode(5)
	node6 = ListNode(6)
	
	
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5
	node5.next = node6
	node6.next = node2
	print(hasCycle(node1))

