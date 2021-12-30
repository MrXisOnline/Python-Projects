
class TestClass:
	def __init__(self, a=None, result=None):
		if type(result) == int:
			self.a = result
			self.result = result
		elif type(a) == int:
			self.a = a
			self.result = result
		else:
			self.a = a
			self.result = result


	def Add(self,b):
		return TestClass(self.a, self.a+b)

	def Sub(self,b):
		return TestClass(self.a, self.a-b)
		

	def Mul(self,b):
		return TestClass(self.a, self.a*b)
		

	def Div(self,b):
		return TestClass(self.a, self.a/b)
		

	def results(self):
		return self.result


testobj = TestClass(5)
print(testobj.Add(2).Mul(2).Add(6).results())
