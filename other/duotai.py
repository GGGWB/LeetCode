class Duck(object):                                  # 鸭子类
	def fly(self):
		print("鸭子沿着地面飞起来了")

class Swan(object):                                  # 天鹅类
	def fly(self):
		print("天鹅在空中翱翔")

class Plane(object):                                 # 飞机类
	def fly(self):
		print("飞机隆隆地起飞了")

def fly(obj):                                        # 实现飞的功能函数
	obj.fly()

duck = Duck()
fly(duck)

swan = Swan()
fly(swan)

plane = Plane()
fly(plane)
