# class A:
# 	explanation = 'this is my program'
# 	def normalMethod(self, name):
# 		print(self.explanation)
# 		# print(name)
# 	@classmethod
# 	def classMethod(cls, explanation):
# 		print(cls.explanation)
# 	@staticmethod
# 	def staticMethod(explanation):
# 		print(explanation)
# a = A()
# a.explanation = 'this is new'
# print(a.normalMethod('explanation'))
# print(A.normalMethod('explanation'))
class Screen(object):
	__resolution = 786432
	@property
	def width(self):
		return self.__width
	@width.setter
	def width(self, width):
		self.__width = width
	@property
	def longth(self):
		return self.__longth
	@longth.setter
	def longth(self, longth):
		self.__longth = longth
	@property
	def resolution(self):
		return self.__resolution

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
	print('测试通过!')
else:
	print('测试失败!')
