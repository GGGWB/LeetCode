class gradapa(object):
	def __init__(self,money):
		self.money = money
	def p(self):
		print("this is gradapa")

class father(gradapa):
	def __init__(self,money,job):
		super().__init__(money)
		self.job = job
	def p(self):
		print("this is father,我重写了父类的方法")

class mother(gradapa):
	def __init__(self, money, job):
		super().__init__(money)
		self.job = job
	
	def p(self):
		print("this is mother,我重写了父类的方法")
		return 100

#定义一个函数，函数调用类中的p()方法
def fc(obj):
	return obj.p()
gradapa1 = gradapa(3000)
father1 = father(2000,"工人")
mother1 = mother(1000,"老师")

fc(gradapa1)            #这里的多态性体现是向同一个函数，传递不同参数后，可以实现不同功能.
fc(father1)
a = fc(mother1)
print(a)