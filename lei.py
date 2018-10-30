class A():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def add(self):
		return self.a+self.b

count=A(3,5)
print(count.add())
		
class B(A):

	def sub(self):
		return self.a-self.b

print(B(3,5).sub())
		